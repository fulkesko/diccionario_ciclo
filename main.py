from dicc_inici import *


while(True):
    menu()
    opcion = input("eliga un opción: ")
    opcion = opcion.lower()
    print("----------------------------")

    if (opcion == "a"):
        ingreso()
    elif (opcion == "b"):
        mostrar()
    elif (opcion == "c"):
        break
print ("vuelva pronto")



