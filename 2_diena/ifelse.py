"""
if <boolean loģika>:
    darbs, kas jāveic, ja True
else:
    darbs, kas jāveic, ja False



if <boolean loģika>:
    darbs, kas jāveic, ja True

"""

vecums = int(input("Cik tev gadu? "))

if vecums >= 18:
    print("Apsveicu, tu esi pilngadīgs!")
    print("Super!")
else:
    print("Tev vēl jāpaaugas!")


if vecums > 65:
    print("Tev laiks doties pensijā!")


if vecums < 10:
    print("Pirmā desmitgade")
elif vecums < 20:
    print("Otrā desmitgade")
elif vecums < 30:
    print("Trešā desmitgade")
elif vecums < 40:
    print("Ceturtā desmitgade")
elif vecums < 50:
    print("Piektā desmitgade")
elif vecums < 60:
    print("Sestā desmitgade")
else:
    print("Kāda vairs starpība....")

# if vecums < 10:
#    print("Pirmā desmitgade")    

# if vecums > 10 and vecums < 20:
#     print("Otrā desmitgade")

# if vecums > 20 and vecums < 30:
#     print("Trešā desmitgade")    

if vecums < 10:
    print("Pirmā desmitgade")
else:
    if vecums < 20:
        print("Otrā desmitgade")
    else:
        if vecums < 30:
            print("Trešā desmitgade")
        else:
            if vecums < 40:
                print("Ceturtā desmitgade")
            else:
                print("......")

# Saīsinātais if pieraksts
print("Esi pilngadīgs") if vecums >= 18 else print("Paaudzies")


