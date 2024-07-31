from tkinter import *
import string
import random
def callback():
    result.config(text=passgen())

def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance, val.get()))
    
root = Tk()
root.title("Random Password Generator Tool")
root.geometry("350x250")

Label(root, text="Choose the strenght of your password",fg="white",bg='blue',font = ('Helvtica',15)).pack()

choice = IntVar()
rb1 = Radiobutton(root, text="Poor Password", variable=choice, value=1)
rb1.pack()
rb2 = Radiobutton(root, text="Average Password", variable=choice, value=2)
rb2.pack()
rb3 = Radiobutton(root, text="Strong Password", variable=choice, value=3)
rb3.pack()

Label(root, text="Choose the Strength of your Password").pack(pady=15)

val = IntVar()
spinlength = Spinbox(root, from_=8, to=30, textvariable=val, width=15)
spinlength.pack()

button_submit = Button(root, text="Generate Password", command=callback)
button_submit.pack(pady=10)

result = Message(root, text="", relief=RAISED, width=200, font=25)
result.pack(side=BOTTOM)

poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
advance = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

root.mainloop()