# accounts.py
# Program that takes a 10-character account number and displays it with only the last 4 digits visible, while first 6 digits are replaced with Xs
# Author: Noemi Diaz


# Step 1: Prompt the user account number

account_number = (input ("Please enter an 10 digit account number:"))

# Step 2: Checking the default account lenght

if len(account_number) !=10:
    print("10")

# Step 3: Masking account number replacing first characters with 'X' and visualizing last 4 digits

masked_account = "X" * 6 + account_number[-4:]
print("Masked Account Number:", masked_account)



# EXTRA TASK
# Program to deal with accounts numbers with any type of length and mask last 4 digit


# Assumption 1: account number less than 4 digit It will turn to an error

# Assumption 2: account number with 4 or more digits (any length) It will mask last 4 numbers with 'X's


    # Step 1: Define the function

def hide_last_4_digits(creditcard_number):

    # Step 2: Check if the length of credit card is not shorter than 4 digits

    if len(creditcard_number) < 4: 
     return "Account number is too short to hide last 4 digits."

    #Step 3: Mask last 4 digit of credit card

    masked_number = "X" * (len(creditcard_number) - 4) + creditcard_number[-4:]
    return masked_number

    # Step 4: User insert credit card number

creditcard_number = (input ("Please enter any length account number:"))

    # Step 5: Finally returns the masked credit card number

masked_creditcard_number = hide_last_4_digits(creditcard_number)

print("Masked credit Card Number:", masked_creditcard_number)






