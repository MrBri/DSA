#!/bin/bash

# Set the name of the output zip file
ZIP_FILE="Prob_folders.zip"

# Find all directories starting with "Prob_" and zip them into the output file
find . -type d -name "Prob_*" -print0 | xargs -0 zip -r $ZIP_FILE

