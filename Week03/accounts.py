# accounts.py
# Program that takes a 10-character account number and displays it with only the last 4 digits visible, while first 6 digits are replaced with Xs
# Author: Noemi Diaz

# Step 1: Input account number

account_number = input ("1020304050")

# Step 2: Checking the account number lenght

if len(account_number) !=10:
    print("1020304050")


# Step 3: Masking account number replacing first characters with 'X'
    
    masked_number = "X" * 6 + account_number[-4:]
    print("Masked Account Number:", masked_number)