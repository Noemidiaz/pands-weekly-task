# bank.py
# Program reads two money amounts and print the answer with a Euro sign
# Author: Noemi Diaz

#Promt the user money amount

amount1 = int (input ('Please enter the first number:'))

amount2 = int (input ('Please enter the second number:'))

newNumber= ((amount1 + amount2)/ 100)


# Print out the answer in a human readable with a euro sign

price = newNumber
txt = "The price is {}€ Euros"
print (txt.format (price))
