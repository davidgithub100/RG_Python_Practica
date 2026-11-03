lista1=(["dato1", "dato2", "dato3", 123, 456, 789, True, False])
lista2=([23,234,5435,32,45,6,0,12,43,11,4])
print(len(lista1)) #len: funcion que nos indica cuantos caracteres tiene un str o cuantos datos tiene una list.

lista1.append("dato4") #append: agraga un dato a la lista.
print(lista1)
print(len(lista1))

lista1.insert(2,4.89) #insert: agraga un dato de la lista por su indice.
print(lista1)
print(len(lista1))

lista1.extend(["hola1","hola2","hola3",987,654,321,]) #extend: agrega una lista a la lista.
print(lista1)
print(len(lista1))

lista1.pop(4) #pop: elimina datos por su indice.
print(lista1)
print(len(lista1))
lista1.pop(-4) #pop: con numeros negativos elimina datos en sentido contrario. 
print(lista1)
print(len(lista1))

lista1.remove(True) #remove: elimina dato por su dato.
print(lista1)
print(len(lista1))

lista2.sort() #sort: organiza en orden las listas numericas.
print(lista2)
print(len(lista2))

lista2.reverse() #reverse: cambia el orden del primero al ultimo en reversa.
print(lista2)
print(len(lista2))

lista1.clear() #clear: elimina todos los datos de la lista.
print(lista1)
print(len(lista1))