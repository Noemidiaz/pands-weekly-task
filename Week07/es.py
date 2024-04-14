# es.py
# This program  reads a text file and displays the count of the letter 'e' it contains
# Author: Noemi Diaz

# The sys module lets access to System-Specific Parameters and Functions (sys.argv), enabling directly access to command-line arguments on Python from script.

import sys

filename = 'mobydick.txt'

def count_es(filename):
    try :
        with open ('mobydick.txt', 'r') as file:
            # Read the contents of the file
            text = file.read()
            # Count occurrences of 'e' (both uppercase and lowercase)
            count = text.lower().count('e')
            return count
    except FileNotFoundError:
        print("Error:File not found.")
        

