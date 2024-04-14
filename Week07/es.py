# es.py
# This program  reads a text file and displays the count of the letter 'e' it contains
# Author: Noemi Diaz




def count_letter_in_file(filename, letter):
    
    try :
        # open the file in read mode
        with open (filename, 'r') as file:

            # Read the contents of the file
            text = file.read()

            # Count occurrences of 'letter' (both uppercase and lowercase)
            count = text.count(letter)
            return count
        
    except FileNotFoundError:
        print("Error:File not found.")
        return -1
    
# File path / filename of the text file. Prompt the user name of file
filename = input("Enter the name of the text file: ")

# Asking for the letter to count
count_letter_in_file = input("which letter would you like to count?: ")

# Function to result the ocurrences of 'Letter'
result = count_letter_in_file(filename)

# Display result 
if result != -1:
    print (f"The letter'{letter_to_count}' appears {result} times in the file.")
    


        
