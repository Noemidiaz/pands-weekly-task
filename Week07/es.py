# es.py
# This program  reads a text file and displays the count of the letter 'e' it contains
# Author: Noemi Diaz




def count_letter_in_file(filename, letter):
    try :
        with open ('mobydick.txt', 'r') as file:
            # Read the contents of the file
            text = file.read()
            # Count occurrences of 'e' (both uppercase and lowercase)
            count = text.lower().count('e')
            return count
    except FileNotFoundError:
        print("Error:File not found.")
        
