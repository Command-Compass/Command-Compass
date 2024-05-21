#!/bin/bash

# Specify the directory path where your files are located
directory="cli_help_files"

# Navigate to the directory
cd "$directory" || exit

# Loop through each file in the directory
for file in *_help.*; do
    # Check if the file exists
    if [ -e "$file" ]; then
        # Get the file extension
        extension="${file##*.}"
        # Remove "_help" from the file name
        new_name="${file%_help*}.$extension"
        # Rename the file
        mv "$file" "$new_name"
        echo "Renamed $file to $new_name"
    else
        echo "No files found matching pattern *_help.*"
    fi
done
