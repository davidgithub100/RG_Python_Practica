#Una matriz es un conjunto de datos

#list es un conjunto de datos que se puede modificar
lista = ["santiago.carreroo", "youtube", "instagram", "tiktok", "facebook"]
print(lista)

lista = ["santiago.carreroo", "youtube", "instagram", "tiktok", "facebook"]
print(lista[0], lista[2], lista[3])

#tupla es un conjunto de datos que no se puede modificar
tupla= ("santiago.carreroo", "youtube", "instagram", "tiktok", "facebook")
print(tupla)
#tupla[0] = "santiago.carrero" # Esto causaría un error
print(tupla)

#conjunto es un conjunto de datos que no se puede modificar por indice ni tiene orden
conjunto = {"santiago.carreroo", "youtube", "instagram", "tiktok", "facebook"}
print(conjunto)
#conjunto[0] = "santiago.carrero"  # Esto causaría un error
#no se puede repetir el mismos dato en un conjunto
conjunto={"cambiando el dato", "por otro difernete", 3232, 0.732}
#conjunto={"cambiando el dato","cambiando el dato", "por otro difernete", 3232, 0.732} #esto causaría un error
print(conjunto)

#diccionario es un conjunto de datos que se puede modificar
#se puede asociar un nombre la clave
diccionario = {
    'nombre': "santiago",
    'edad': "24",
    'ciudad': "Bogotá",
    'estado': "aun la extraño"
}
diccionario["clave"] = "valor"
#diccionario[2]="0", #esto causaría un error
#diccionario["nombre"] = 0.0, 

print(diccionario)