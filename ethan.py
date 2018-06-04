telefono = list()
nombre = list()

while(True):
    nom = input("ingrese nombre: ")
    if (nom == "salir"):
        break
    nombre.append(nom)
    tel = (int(input("ingrese numero del telefono: ")))
    telefono.append(tel)


listacontactos = zip(nombre, telefono)

for i in listacontactos:
    print(i)
