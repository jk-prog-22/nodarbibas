# variants, kā importēt garākus nosaukumus
import mape.helper as helper

# importē konkrētu funkciju, tā it kā tā būtu lokāli definēta
#from helper import ievadiSkaitli

def main():
    sk1 = helper.ievadiSkaitli()
    sk2 = helper.ievadiSkaitli()

    print("Ievadīto skaitļu summa ir", sk1 + sk2)
    helper.pievienotFailam("summa.dat", sk1 + sk2)



#print(__name__)
if __name__ == '__main__':
    main()
else:
    print("Šī programma nav domāta importam")