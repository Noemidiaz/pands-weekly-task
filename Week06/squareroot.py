# squareroot.py
# Create a program that takes a floating positive number and gives an approximate square root using Newton's method
# Author: Noemi Diaz

# Defining function as sqrt
def sqrt(number):
   
    # Initial estimation for the square root
    estimateData = number / 2

    # Continue iterating until the estimation is sufficiently accurate
    while abs(estimateData * estimateData - number) > 0.0001:
     
        # Improving the estimation using Newton's method
        estimateData = (estimateData + number / estimateData) / 2 
    
    return estimateData

# Request user number
number = float(input("Enter a positive floating-point number: "))
if number < 0:
    print("Please enter a positive number.")
else:
    result = sqrt(number)
    print("Square root approximation:", result)
