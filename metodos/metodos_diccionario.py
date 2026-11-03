diccionario={
    'nombre':"david",
    'estado':"roto",
    'sueño':"q todo valga la pena"
}

k=diccionario.keys() #keys: retorna las claves en orden de indice.
print(k)

g=diccionario.get('sueño') #get: retorna el valor de la clave que le indiquemos.
print(g)

diccionario.pop('nombre') #pop: elimina una clave y su valor, osea un dato.
print(diccionario)

i=diccionario.items() #items: retorna los datos divididos por grupos.
print(i)

diccionario.clear() #clear: elimina todos los datos.
print(diccionario)