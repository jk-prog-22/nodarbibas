from tkinter import *

root = Tk()
root.geometry("200x100")
root.title("Pogas")

def pogaNospiesta():
    print("Poga tika nospiesta!")
    Label(root, text="Pogas spaidītājs!").pack()

poga = Button(root, text="Nospied mani!", command=pogaNospiesta, padx=40, pady=20)
poga.pack()


root.mainloop()