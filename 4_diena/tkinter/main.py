from tkinter import *

root = Tk()
root.title("Skaitītājs")

def pievienot():
    try:
        skaitlis = int(ievade.get())
        kluda.grid_forget()
    except ValueError:
        kluda.grid(row=2, column=0)        
        #print("Kļūda! Lūdzu ievadi skaitli!")
        return

    rez = int(rezultats.cget("text"))
    rez = rez + skaitlis
    rezultats.config(text=rez)


def starpiba():
    try:
        skaitlis = int(ievade.get())
        kluda.grid_forget()
    except ValueError:
        kluda.grid(row=2, column=0)
        #print("Kļūda! Lūdzu ievadi skaitli!")
        return

    rez = int(rezultats.cget("text"))
    rez = rez - skaitlis
    rezultats.config(text=rez)

def reset():
    rezultats.config(text="0")
    kluda.grid_forget()

ievade = Entry(root)
pieskaitit = Button(root, text="+", command=pievienot, padx=20)
atnemt = Button(root, text="-", command=starpiba, padx=20)
rst = Button(root, text="Reset", command=reset, padx=20)
rezultatsLb = Label(root, text="Rezultāts:")
rezultats = Label(root, text="0")
kluda = Label(root, text="Kļūda! Lūdzu ievadi skaitli!")

ievade.grid(row=0, column=0, columnspan=2)
pieskaitit.grid(row=0, column=2)
atnemt.grid(row=1, column=2)
rst.grid(row=0, column=3, rowspan=2)
rezultatsLb.grid(row=1, column=0)
rezultats.grid(row=1, column=1)

root.mainloop()