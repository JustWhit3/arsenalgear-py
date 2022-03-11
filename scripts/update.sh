#!/bin/bash

#====================================================
#     UPDATING THE REPOSITORY
#====================================================
echo ""
echo "Updating the repository..."
echo ""

#Deleting old files and downloading the new repo:
cd ..
rm -rf arsenalgear*

#Downloading new ones:
wget https://github.com/JustWhit3/arsenalgear/archive/main.zip
mv main.zip arsenalgear-main.zip
unzip arsenalgear-main.zip
rm arsenalgear-main.zip
mv arsenalgear-main arsenalgear
echo ""
echo "Repository is up-to-date!"
echo ""
echo "Enter the following commands:"
echo "1. cd .."
echo "2. cd arsenalgear"
echo ""