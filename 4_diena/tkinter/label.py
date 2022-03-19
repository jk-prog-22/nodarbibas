from tkinter import *

root = Tk()
root.title("Mans logs")

nosaukums = Label(root, text="Teksts iekš loga!")
vards = Label(root, text="Pavasaris")
#atstarpe = Label(root, text=" ")

#Elementi, kas anonīmi veidoti tiem pēc tam nevar piekļūt.
Label(root, text=" ").grid(row=0, column=3)
Label(root, text=" ").grid(row=1, column=1)

#nosaukums.pack() # Automātiski parādīt elementu
#vards.pack()

nosaukums.grid(row=0, column=4)
#atstarpe.grid(row=0, column=3)
vards.grid(row=1, column=2)
#atstarpe.grid(row=1, column=1)

root.mainloop()