# A program that reads a digit 0-9 from the user and prints its name
# Therefore, user inputs a number digit between 0-9.
# Create a vaiable that lists the names of each number digits in their order.
# Use an f string to embed the expression of num inside the num_digits


def name_digit():
    num = int(input( "Enter a number between 0-9 : "))
    num_digits = ("zero", "One", "Two", "Three", "Four", "Five",
                  "six", "Seven", "Eight", "Nine")
    print (f"The name of digit {num} is {num_digits[num]}")
    

name_digit()
    
