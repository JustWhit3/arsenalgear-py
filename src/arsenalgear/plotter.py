#!/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 12:18:00 2022
Author: Gianluca Bianco
"""

#################################################
#     Libraries
#################################################
from termcolor import colored
from mathematics import e_parser
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as sci
from sklearn.model_selection import learning_curve

#################################################
#     plot_AMS
#################################################
def plot_AMS( predictions, label_vectors, weights ):
    """
    Function used to plot the AMS function.

    Args:
        predictions ( numpy array ): is a binary array, defined from the set of data that we're considering.
        label_vectors ( numpy array ): is a binary array constructed from the dataset, used for each model, that distinguishes an event between signal and background.
        weights ( numpy array ): it takes the weights associated to each data of my dataset.
    """
    
    x = np.arange( 0.5, 1, 1e-2 )
    y = np.array( [ AMS_score( x_values, predictions, label_vectors, weights ) for x_values in x ] )
    
    plt.plot( x, y )
    plt.xlabel( "Cut Parameter" )
    plt.ylabel( "AMS Score" )
    plt.grid()
    
    print( "The best AMS Score is {:.3f} at a Cut Parameter of {:.2f}".format( max( y ), x[ np.argmax( y ) ] ) )

#################################################
#     plotter_complex
#################################################
def plotter_complex( real_part, imaginary_part, a, b, n, coefficient ):
    """
    Function used to plot a given function for an index n.
    Args:
        real_part (string): mathematical real expression part.
        imaginary_part (string): mathematical imaginary expression part.
        a (any): lower integration extreme.
        b (any): higher integration extreme.
        n (int): wave function index.
        coefficient (any): value of the normalization coefficient.
    Returns:
        plot: the wave-function plot for the index n is returned.
    """
    
    if coefficient != colored( "Error, division by 0!", "red" ):
        
        if a == -np.inf and b != np.inf:
            x = np.arange( -10, b, ( ( b+10 ) / 10 ) )
        elif a != -np.inf and b == np.inf:
            x = np.arange( a, 10, ( ( 10-a ) / 10 ) )
        elif a == -np.inf and b == np.inf:
            x = np.arange( -10, 10, ( ( 20 ) / 10 ) )
        else:
            x = np.arange( 10*a, 10*b, ( ( 10*( b-a ) ) / 10 ) )

        def func( x ):
            return coefficient * e_parser( real_part, imaginary_part, n, x )
        
        my_label = "Normalized wave-function f(x) for n = " + str( n )
        plt.figure( figsize = ( 8, 6 ), dpi = 80 )
        plt.xlabel( "Re: f(x)" )
        plt.ylabel( "Im: f(x)" )
        plt.title( my_label )

        if real_part == "0" and imaginary_part != "0":
            X_Y_Spline = sci.make_interp_spline( x, np.imag( func( x ) ) )
            X = np.linspace( x.min(), x.max(), 500 )
            Y = X_Y_Spline( X )
        
            plt.xlabel( "x" )
            plt.ylabel( "Im: f(x)" )
            plt.plot( X, Y, color = "green" )
        elif real_part != "0" and imaginary_part == "0":
            X_Y_Spline = sci.make_interp_spline( x, np.real( func( x ) ) )
            X = np.linspace( x.min(), x.max(), 500 )
            Y = X_Y_Spline( X )
        
            plt.xlabel( "x" )
            plt.ylabel( "Re: f(x)" )
            plt.plot( X, Y, color = "green" )
        else:
            X = np.real( func( x ) )
            Y = np.imag( func( x ) )
            tck, u = sci.splprep( [ X, Y ], s = 0 )
            unew = np.arange( 0, 1.01, 0.01 )
            out = sci.splev( unew, tck )
            
            plt.plot( X, Y, 'x', out[0], out[1], color = "green" )

        plt.show()

#################################################
#     plot_learning_curve
#################################################
def plot_learning_curve( estimator, title, X, y, axes = None, ylim = None, cv = None, n_jobs = None, scoring = None, train_sizes = np.linspace( 0.1, 1.0, 5 ), ):
    """
    Generate 3 plots: the test and training learning curve, the training samples vs fit times curve, the fit times vs score curve. Taken from here: https://scikit-learn.org/stable/auto_examples/model_selection/plot_learning_curve.html.
    Args:
        estimator (sklearn): An estimator instance implementing `fit` and `predict` methods which
        will be cloned for each validation.
        title (str): Title for the chart.
        X (numpy.array): array-like of shape (n_samples, n_features). Training vector, where ``n_samples`` is the number of samples and
        ``n_features`` is the number of features.
        y (numpy.array): array-like of shape (n_samples) or (n_samples, n_features). Target relative to ``X`` for classification or regression;
        axes (numpy.array, optional): array-like of shape (3,). Axes to use for plotting the curves. Defaults to None.
        ylim (numpy.array, optional): tuple of shape (2,). Defines minimum and maximum y-values plotted, e.g. (ymin, ymax). Defaults to None.
        cv (int, optional): cross-validation generator or an iterable. Determines the cross-validation splitting strategy.
        Possible inputs for cv are:. Defaults to None.
        n_jobs (int, optional): nt or None. Number of jobs to run in parallel. Defaults to None.
        scoring (str, optional): a str (see model evaluation documentation) or a scorer callable object / function with signature
        ``scorer(estimator, X, y)``.. Defaults to None.
        train_sizes (numpy.array, optional): array-like of shape (n_ticks,). Relative or absolute numbers of training examples that will be used to generate the learning curve.. Defaults to np.linspace( 0.1, 1.0, 5 ).
    """

    if axes is None:
        _, axes = plt.subplots( 1, 3, figsize = ( 20, 5 ) )

    axes[0].set_title( title )
    if ylim is not None:
        axes[0].set_ylim( *ylim )
    axes[0].set_xlabel( "Training examples" )
    axes[0].set_ylabel( "Score" )

    train_sizes, train_scores, test_scores, fit_times, _ = learning_curve( estimator, X, y, scoring = scoring, cv = cv, n_jobs = n_jobs, train_sizes = train_sizes, return_times = True, )
    train_scores_mean = np.mean( train_scores, axis = 1 )
    train_scores_std = np.std( train_scores, axis = 1 )
    test_scores_mean = np.mean( test_scores, axis = 1 )
    test_scores_std = np.std( test_scores, axis = 1 )
    fit_times_mean = np.mean( fit_times, axis = 1 )
    fit_times_std = np.std( fit_times, axis = 1 )

    # Plot learning curve
    axes[0].grid()
    axes[0].fill_between( train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha=0.1, color="r", )
    axes[0].fill_between( train_sizes, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std, alpha = 0.1, color = "g", )
    axes[0].plot( train_sizes, train_scores_mean, "o-", color = "r", label = "Training score" )
    axes[0].plot( train_sizes, test_scores_mean, "o-", color = "g", label = "Cross-validation score" )
    axes[0].legend( loc = "best" )

    # Plot n_samples vs fit_times
    axes[1].grid()
    axes[1].plot( train_sizes, fit_times_mean, "o-" )
    axes[1].fill_between( train_sizes, fit_times_mean - fit_times_std, fit_times_mean + fit_times_std, alpha = 0.1, )
    axes[1].set_xlabel( "Training examples" )
    axes[1].set_ylabel( "fit_times" )
    axes[1].set_title( "Scalability of the model" )

    # Plot fit_time vs score
    fit_time_argsort = fit_times_mean.argsort()
    fit_time_sorted = fit_times_mean[ fit_time_argsort ]
    test_scores_mean_sorted = test_scores_mean[ fit_time_argsort ]
    test_scores_std_sorted = test_scores_std[ fit_time_argsort ]
    axes[2].grid()
    axes[2].plot( fit_time_sorted, test_scores_mean_sorted, "o-" )
    axes[2].fill_between( fit_time_sorted, test_scores_mean_sorted - test_scores_std_sorted, test_scores_mean_sorted + test_scores_std_sorted, alpha=0.1, )
    axes[2].set_xlabel( "fit_times" )
    axes[2].set_ylabel( "Score" )
    axes[2].set_title( "Performance of the model" )
    
    return plt