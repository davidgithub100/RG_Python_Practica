#Ejercicio 1. Pide un número al usuario 
#muestra True si está entre 1 y 100 (inclusive), False si no.
numero = 200
resultado = numero >= 1 and numero <= 100
print(resultado )

#Ejercicio 2. Pide la edad 
#muestra si la persona puede entrar a un evento: debe ser mayor de 18 y menor de 65.
edad= 200
identificador = edad >= 18 and edad <= 65
print(identificador)

#Ejercicio 3. Pide un número 
#di si es par o divisible por 5.
numero = 201
resultado = numero % 2 == 0 or numero % 5 == 0
print(resultado)

#Ejercicio 4. Pide una letra 
#muestra True si es una vocal 
#(usa or con varias comparaciones, o prueba con in "aeiou").
letra = input("letra:").lower()
calibrador = letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"
print(calibrador) 

#Ejercicio 5. Pide una contraseña
#verifica que tenga más de 8 caracteres y que no sea igual a "12345678".
contraseña = input("contraseña: ")
rectificador = len(contraseña) > 8 and contraseña != "12345678"
print(rectificador) 