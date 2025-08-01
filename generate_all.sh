#!/bin/bash

# Check if language argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <language>"
    echo "Example: $0 C"
    exit 1
fi

lang=$1

# Check if the tests directory exists
if [ ! -d "./data/tests" ]; then
    echo "Error: ./data/tests directory not found"
    exit 1
fi

# Iterate through all .yaml files in the tests directory
for file in ./data/tests/*.yaml; do
    # Check if files exist (in case no .yaml files are found)
    if [ ! -e "$file" ]; then
        echo "No .yaml files found in ./data/tests/"
        exit 1
    fi
    
    # Extract filename without path and extension
    item=$(basename "$file" .yaml)
    
    echo "Generating tests for $item with language $lang..."
    
    # Run the Python script
    python3 generate.py "$item" "$lang"
    
    # Check if the command was successful
    if [ $? -ne 0 ]; then
        echo "Error: Failed to generate tests for $item"
        exit 1
    fi
done

echo "All test generations completed successfully!"