#!/usr/bin/env python3
"""
basic serialization module that adds the functionality to serialize
a Python dictionary to a JSON file and deserialize the JSON 
file to recreate the Python Dictionary
"""
import json

def serialize_and_save_to_file(data, filename):
    """Serializes a Python dictionary and saves it to a JSON file."""
    # Your code here to serialize the data and save it to a file
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Loads a JSON file and deserializes it to a Python dictionary."""
    # Your code here to load and deserialize the data from the file
    with open(filename, 'r') as f:
        data = json.load(f)
    return data