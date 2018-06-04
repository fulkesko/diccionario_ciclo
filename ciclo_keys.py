dicc = {}
doc = {'1': "w",'2' : "e", '3' : "a"}

ind = 0

while(True):
   valor = input("algo: ")
   if (valor == "salir"):
       break

   dicc[ind] = valor
   #print(ind)
   #print(dicc)
   ind += 1

dicc.update(doc)

for i in dicc:
    print(i, ":", dicc[i])


"""juntar las mierdas de diccionarios a traves de los indices"""