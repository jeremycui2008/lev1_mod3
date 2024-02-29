"""
 Create an app that tells a joke, then a punchline
"""
import tkinter as tk
import random
from tkinter import messagebox
import pymouse


# Use this function to return a random character
def generate_random_letter():
    return chr(random.randint(0, 25) + ord('a'))


class ChuckleClicker(tk.Tk):
    def __init__(self):
        super().__init__()
        hi=tk.Tk()
        # TODO: Declare and initialize 2 buttons (tk.Button)
        #  one button for the joke and another for the punchline
        robert=tk.Button(hi, text="JOKE")
        # TODO: Place the 2 buttons next to each other (see example image)

        # TODO: Call the joke button's bind() method to call the on_joke()
        #  method when a mouse button is pressed
        #  example: self.joke_button.bind('<ButtonPress>', self.on_joke)
        self.on_joke.bind()
        button = pymouse()


        # TODO: Call the joke button's bind() method to call the on_punchline()
        #  method when a mouse button is pressed

    def on_joke(self, event):
        print('Jwhy did the chicken cross the road')

        # TODO: Write your joke below!

    def on_punchline(self, event):
        print('to be transported to the butchery')


        # TODO: Write a punchline to your joke!


if __name__ == '__main__':
    pass
    # TODO: Create a new ChuckleClicker object and set the title and geometry.
    #  Remember to call mainloop() at the end

