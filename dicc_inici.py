bebos = {'nº' : ["nombre","fecha","hora"]}

def ingreso():
    ind_n = 1

    while(True):
        nom_bb = input("nombre del bebé: ")
        if (nom_bb == "salir"):
            break

        fech_bb = input("fecha de nacimiento: ")
        hora = input("hora de nacimiento ")

        bebos[ind_n] = [nom_bb, fech_bb, hora]

        ind_n += 1
## agregar pregunta "desea continuar ingresando"
def mostrar():
    for a in bebos:

        print(a, ":", bebos[a])

