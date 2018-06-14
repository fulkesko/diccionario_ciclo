from dicc_inici import *
from PIL import Image

while(True):
    menu()
    tamaño = re_nacidos.__len__()
    opcion = input("eliga un opción(a,b o c): ")
    opcion = opcion.lower().strip()
    print("♪   ♪   ♪   ♪   ♪   ♪   ♪   ♪")

    if (opcion.__contains__("a")):
        ingreso()
    elif (opcion.__contains__("b")):
        if (tamaño == 0 ):
            print("aun no hay datos registrados")
            print("estas seguro de querer seguir?")
            confirma = input("s/n: ").lower().strip()
            if (confirma.__contains__("s") or confirma.__contains__("y")):
                mostrar_todo()
        else:
            mostrar_todo()
    elif (opcion.__contains__("c")):
        adios = Image.open("adios.png")
        adios.show()
        break

print ("vuelva pronto")



