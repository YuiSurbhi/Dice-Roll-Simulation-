import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("500x360")
window.config(pady=30)
window.title("Dice Roll")

dice = ["dice-six-faces-one.png","dice-six-faces-two.png","dice-six-faces-three.png","dice-six-faces-four.png","dice-six-faces-five.png","dice-six-faces-six.png"]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window,image=image1)
label2 = tk.Label(window,image=image2)

label1.image = image1
label2.image = image2

label1.place(x = 50, y = 100)
label2.place(x = 300,y = 100)

def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1 

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image = image2

button = tk.Button(window,text="ROLL", bg="black",fg = "white",font="Time 20 bold",command=dice_roll)
button.place(x = 200, y = 0)


window.mainloop()




