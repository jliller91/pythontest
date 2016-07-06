"""
Justin Liller
Magic 8 Ball Instructions:

I'm sure you've used a magic 8 ball at one point in your life. You ask it a question, turn it right side up and it gives
an answer by way of a floating die with responses written on it. You can create one in python. You must:
    1. Allow the user to enter their question
    2. Display an in progress message( i.e. "thinking")
    3. Create 20 responses, and show a random response
    4. Allow the user to ask another question or quit
Bonus - Using whatever module you like, add a gui. Your gui must have:
    1. A box for users to enter the question
    2. At least 4 buttons: Ask , clear(the text box), play again and quit(this must close the window)

7/6/2016
"""
import time
from random import randint

replies = ["Yes", "No", "In the future", "Never", "Are you serious?"]


def question():
        question = input("What is your question?\n")
        print("The answer fades into view...")
        time.sleep(2)
        print(replies[randint(0, 4)])
        repeat()


def repeat():
        print("Would you like ask another question?")
        answer = input().lower()
        if answer == "yes":
            question()

print("You shake the magic 8 ball...")
question()