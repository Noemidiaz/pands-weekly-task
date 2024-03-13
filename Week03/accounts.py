# accounts.py
# Program that takes a 10-character account number and displays it with only the last 4 digits visible, while first 6 digits are replaced with Xs
# Author: Noemi Diaz


# Step 1: Prompt the user account number

account_number = int (input ("Please enter an 10 digit account number:"))

# Step 2: Checking the default account lenght

if len(account_number) !=10:
    print("10")

# Step 3: Masking account number replacing first characters with 'X' and visualizing last 4 digits

account_number = "1020304050"
masked_account = "X" * 6 + account_number[-4:]
print("Masked Account Number:", masked_account)




# EXTRA
# Program to deal with accounts numbers with any type of length

# Assumption 1: account number less than 4 digit It will turn to an error
# Assumption 2: account with any length and mask last 4 digit

"""
creditcard_number = input ("1020304050607080")

if len(creditcard_number) < 4: 
masked_number = "X" * (len(creditcard_number) - 4) + creditcard_number[-4:]

masked_account_number = mask_account_number(creditcard_number)

print("Masked Account Number:", masked_account_number)
"""








