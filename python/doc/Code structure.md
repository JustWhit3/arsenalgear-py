# Code structure

## Table of contents

- [mathematics](#mathematics)
  - [Hermite, Chebyshev, Legendre and Laguerre](#hermite-chebyshev-legendre-and-laguerre)
  - [IsInBounds](#isinbounds)
  - [e_parser](#e_parser)
  - [kronecker](#kronecker)
- [machinelearning](#machinelearning)
  - [AMS_score](#amsscore)
  - [plot_AMS](#plotams)
- [plotter](#plotter)
  - [plotter_complex](#plotter_complex)

## Math

### Hermite, Chebyshev, Legendre and Laguerre

Module: [mathematics.py](https://github.com/JustWhit3/arsenalgear/blob/main/python/arsenalgear/mathematics.py)

Complete definition: `Hermite( x, n )`, `Chebyshev( x, n )`, `Legendre( x, n )` and `Laguerre( x, n )`.

Usage: it is used to return orthogonal polynomials functions.
> **NOTE**: `numpy` returns only the polynomials coefficients, not functions.

Example usage: `Laguerre( 0.5, 3 )`

### isInBounds

Module: [mathematics.py](https://github.com/JustWhit3/arsenalgear/blob/main/python/arsenalgear/mathematics.py)

Complete definition: `IsInBounds( value, min_, max_ )`

Usage: it is used to check if a value is the bound [`min_`,`max_`].

Example usage: `IsInBounds( 3.2, 1.0, 5.3 )`

### e_parser

Module: [mathematics.py](https://github.com/JustWhit3/arsenalgear/blob/main/python/arsenalgear/mathematics.py)

Complete definition: `e_parser( real_part, imaginary_part, n, x )`

Usage: returns the complex value of a parsed expression.

Example usage: `e_parser( "n*np.cos( x )", "3*n", 2, np.pi )`

### kronecker

Module: [mathematics.py](https://github.com/JustWhit3/arsenalgear/blob/main/python/arsenalgear/mathematics.py)

Complete definition: `kronecker( i, j )`

Usage: returns the kronecker delta value.

Example usage: `kronecker( 2, 2 )`

### AMS_score

Module: [machinelearning.py](https://github.com/JustWhit3/arsenalgear/blob/main/python/arsenalgear/machinelearning.py)

Complete definition: `AMS_score( x_cut, predictions, label_vectors, weights )`

Usage: function used to compute the AMS score.

Example usage: none

### plot_AMS

Module: [machinelearning.py](https://github.com/JustWhit3/arsenalgear/blob/main/python/arsenalgear/machinelearning.py)

Complete definition: `plot_AMS( predictions, label_vectors, weights )`

Usage: function used to plot the AMS function.

Example usage: see [here](https://github.com/JustWhit3/higgs-decay-classification/blob/master/scripts/python/analysis.py)

### plotter_complex

Module: [plotter.py](https://github.com/JustWhit3/arsenalgear/blob/main/python/arsenalgear/plotter.py)

Complete definition: `plotter_complex( real_part, imaginary_part, a, b, n, coefficient )`

Usage: function used to plot a complex function.

Example usage: see [here](https://github.com/JustWhit3/WaveNCC)

### MultiProcesses

Module: [parallelization.py](https://github.com/JustWhit3/arsenalgear/blob/main/python/arsenalgear/parallelization.py)

Complete definition: `MultiProcesses( *functions ):`

Usage: function used to sent more processes in parallel.

Example usage: `MultiProcesses( process_1, process_2 )`