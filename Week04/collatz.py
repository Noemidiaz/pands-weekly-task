# collatz.py
# In this program the user enter any positive integer and the program ends when the value is 1
#Author:Noemi Diaz



# Definitizion of function 'collatz' with a 'number' value

def collatz (number):

   # Adding a loop using 'while' until the number becomes 1
    while number > 1:
        print (number, end=' ')
      
       # n is odd
        if (number % 2):
            number = number * 3 + 1  
       
        # n is even
        else:
            number = number//2
    print(1, end=' ')


# Ask user to enter a number- Integer

number = int (input ('Enter number:'))

# Print each step of the sequence until the value becomes 1
print ('sequence: ', end= ' ')

collatz(number)
