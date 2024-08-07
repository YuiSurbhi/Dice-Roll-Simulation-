import tkinter as tk
from PIL import Image, ImageTk
import random

# Create the main window 
window = tk.Tk()
window.geometry("500x360")
window.title("My Two Dice Rollers")

# List of file path for dice images 
dice = ["C:/Users/HP/Pictures/dice1.png","C:/Users/HP/Pictures/dice2.png","C:/Users/HP/Pictures/dice3.png","C:/Users/HP/Pictures/dice4.png","C:/Users/HP/Pictures/dice5.png","C:/Users/HP/Pictures/dice6.png"]

# Loading the initial images for dice 
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# Create labels to display dice images 
label1 = tk.Label(window,image=image1)
label2 = tk.Label(window,image=image2)

label1.image = image1     # Keep a reference to avoid garbage collection
label2.image = image2     # Keep a reference to avoid garbage collection

# Place the dice image labels on the window 
label1.place(x = 40, y = 100)
label2.place(x = 300,y = 100)

# create function to roll the dice and update the labels with new images 
def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1     # Keep the reference to the new image 

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image = image2     # Keep the reference to the new image 

# Create and place the roll button attaching roll_dice function 
button = tk.Button(window,text="ROLL", bg="black",fg = "white",font="Time 20 bold",command=dice_roll)
button.place(x = 200, y = 0)

# Start the tkinter event loop
window.mainloop()




