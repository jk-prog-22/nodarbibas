from tkinter import *

root = Tk()
root.geometry("200x500")
root.title("Pogas")

def pogaNospiesta():
    print(ievade.get())
    Label(root, text=ievade.get()).pack()
    ievade.delete(0, END)

poga = Button(root, text="Apstiprināt", command=pogaNospiesta, padx=40, pady=20)
ievade = Entry(root)



ievade.pack()
poga.pack()


root.mainloop()