from dicc_inici import *


while(True):
    menu()
    opcion = input("eliga un opción: ")
    opcion = opcion.lower().strip()
    print("----------------------------")

    if (opcion.__contains__("a")):
        ingreso()
    elif (opcion.__contains__("b")):
        mostrar_todo()
    elif (opcion.__contains__("c")):
        break
        
print ("vuelva pronto")



