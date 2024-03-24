# collatz.py
#
#Author:Noemi Diaz



# Definitizion of variable and sequence depending if number is even or odd

def collatz (number):
    while number > 1:
        print (number, end='')
       # n is even
        if number % 2 == 0:
            number = number // 2
        # n is odd
        else:
            number = number * 3 + 1
    print(1)

# Ask user to enter a number- Integer

n = int (input ('Enter number:'))

print (number,end= '')

collatz(number)

