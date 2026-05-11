# DevReady2Backend
This is a Python Backend Project which makes usage of JSON file.

# Data
The 13 dictionaries in JSON file contains some calls using attributes like id, direction, call_type(missed, answered or voicemail),duration, archived calls(Boolean) and dates.

# Load Data
In the file read_data.py, I read the JSON file and load the data in a list/array.

# Core Functions
I wrote 3 basic functions which use the list of the dictionaries in order to return all the non-archived calls, to find a dictionary using as a parameter the id(unique) and find a non-archived calls using id.

# Answered Calls
From answered calls, I found which calls were quicker than other calls(using 30min as margin) and deleted some of them with bigger duration(using 50min as margin)

# Testing
I verified all functions from each file in a separate test script.
