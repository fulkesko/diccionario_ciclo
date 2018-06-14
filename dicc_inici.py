from datetime import datetime
from PIL import Image

re_nacidos = list()

def ingreso():
    bebos = dict()
    fecha_actu = datetime.now()
    formato_fecha = "%d/%m/%Y"
    edad = list()
    while(True):

        nombre = input("nombre del bebé: ").strip().lower()
        while(nombre == ""):
            nombre = input("ingrese un nombre!!!: ")
        bebos['nom'] = nombre


        fecha_nac = datetime.strptime(input("ingrese fecha (dia/mes/año): "), formato_fecha)
        while(fecha_actu < fecha_nac):
            fecha_nac = datetime.strptime(input("ingrese una fecha valida!! (dia/mes/año): "), formato_fecha)

        diferencia = fecha_actu - fecha_nac
        anios = (diferencia / 365)
        anios = anios.days
        edad.append(anios)
        meses = diferencia / 12
        meses = meses.days
        edad.append(meses)
        dias = diferencia.days
        edad.append(dias)


        bebos['edad'] = edad
        re_nacidos.append(bebos)

        opcion = input("desea seguir ingresando? (s/n):")
        if (opcion.__contains__("n")):
            break
        bebos = dict()
        edad = list()

def mostrar_todo():
    tamaño = re_nacidos.__len__()

    if(tamaño == 0):
        portada = Image.open("nada.jpg")
        portada.show()
    else:
        for nin in re_nacidos:
            print("nombre: ",nin['nom'])
            print("edad: ")
            print("     ",nin['edad'][0],"años")
            print("     ",nin['edad'][1],"meses")
            print("     ",nin['edad'][2],"dias")
            print("♪   ♪   ♪   ♪   ♪   ♪   ♪   ♪")
def menu():
    print(" ")
    print("sistema de registro de recien nacidos")
    print("a) ingreso de recien nacido ")
    print("b) mostrar bebés ")
    print("c) salir")
    print("♪   ♪   ♪   ♪   ♪   ♪   ♪   ♪")
