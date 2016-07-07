"""
Justin Liller
Coin Estimator Instructions:

When some people receive change after shopping, they put it into a container and let it add up over time. Once they fill
 up the container, they'll roll them up in coin wrappers which can then be traded in at a bank for what they are worth.
 While most banks will give away coin wrappers for free, it's convenient to have an idea of how many you will need.
 Instead of counting how many coins you have, it's easier to separate all of your coins, weigh them, and then estimate
 how many of each type you have and then how many wrappers you'll need.

For example, if you weigh all of your dimes and see that you have 1276.9g of them, you can estimate that you have about
563 dimes (since each one is 2.268g) and you would be able to fill 11 dime wrappers.

Goal:
Create a program that allows the user to input the total weight of each type of coin they have (pennies, nickels, dimes,
 and quarters), and then print out how many of each type of wrapper they would need, how many coins they have, and the
 estimated total value of all of their money.
Weight of each coin and how many fit inside each type of wrapper.

Subgoals:
Round all numbers printed out to the nearest whole number.
Allow the user to select whether they want to submit the weight in either grams or pounds.


7/7/2016
"""
import math

penny = input("How much do your pennies weigh?\n")
nickel = input("How much do your nickels weigh?\n")
dime = input("How much do your dimes weigh?\n")
quarter = input("How much do your quarters weigh?\n")

print("\nStarting Coin Estimator")
if penny > str(1):
    print("You have %s pennies." % penny)
elif penny == str(1):
    print("You have %s penny." % penny)
else:
    print("You have no pennies.")

if nickel > str(1):
    print("You have %s nickels." % nickel)
elif nickel == str(1):
    print("You have %s nickel." % nickel)
else:
    print("You have no nickels.")

if dime > str(1):
    print("You have %s dimes." % dime)
elif dime == str(1):
    print("You have %s dime." % dime)
else:
    print("You have no dimes.")

if quarter > str(1):
    print("You have %s quarters." % quarter)
elif quarter == str(1):
    print("You have %s quarter." % quarter)
else:
    print("You have no quarters.")


pennywraps = int(penny)/50
print("\nYou will need " + str(math.floor(pennywraps)) + " penny wrappers")

nickelwraps = int(nickel)/40
print("You will need " + str(math.floor(nickelwraps)) + " nickel wrappers")

dimewraps = int(dime)/50
print("You will need " + str(math.floor(dimewraps)) + " dime wrappers")

quarterwraps = int(quarter)/50
print("You will need " + str(math.floor(quarterwraps)) + " quarter wrappers")