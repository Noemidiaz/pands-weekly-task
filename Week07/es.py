# es.py
# This program  reads a text file and displays the count of the letter 'e' it contains
# Author: Noemi Diaz



# Defining function
def count_letter_in_file(filename, letter):
    
    try :
        # open the file in read mode
        with open (filename, 'r') as file:

            # Read the contents of the file
            text = file.read()

            # Count occurrences of 'letter' 
            count = text.count(letter)
            return count
    # Checking is file is found or not. If not, It will appears Error message   
    except FileNotFoundError:
        print("Error:File not found.")
        return -1
    
# Prompt the user name of file (file path)
filename = input("Enter the name of the text file: ")

# Asking user for the letter to count (It's possible to count uppercase or lowercase letter)
letter_to_count = input("which letter would you like to count?: ")

# Function to result the ocurrences of 'Letter'
result = count_letter_in_file(filename, letter_to_count)

# Display result 
if result != -1:
    print (f"The letter'{letter_to_count}' appears {result} times in the file.")
    


        
