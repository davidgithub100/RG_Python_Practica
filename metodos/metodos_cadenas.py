#DATO.METODO()
dato = "datodatodatodato"
print(dato.upper()) #upper: convierte letras en mayusculas.
print(dato.lower()) #lower: convierte letras en minusculas.
print(dato.capitalize()) #capitalize: comvierte la primera en mayuscula y lo demas en miuzcula
print(dato.isnumeric()) #isnumeric: valida el dato y si es numerico arroja true, si no false.
print(dato.isalpha())   #isalpha: valida el dato y si es alphanumerico arroja true, si no false.

print(dato.find("dato")) #find: busca un dato o un fragmento de dato en el dato que le solicitamos y nos retorna su pocicion. De lo contrario retorna -1.
print(dato.index("dato")) #index: busca un dato o un fragmento de dato en el dato que le solicitamos y nos retorna su pocicion. De lo contrario retorna excepcion.
print(dato.count("dato")) #count: busca el dato o un fragmento de dato en el dato que le solicitamos y nos retorna la cantidad de veces que esta.

print(dato.startswith("d")) #startswith: valida si el dato comiensa asi, nos arroja true o false en caso de q no.
print(dato.endswith("o"))   #endwith: valida si el dato finaliza asi, nos arroja true o false en caso de q no.

print(dato.replace("at","altonic")) #replace: cambia el fragmento de dato indicado por el nuevo fragmento de dato indicado, separado por comas (se cambia la cantidad de veces encontrado).
print(dato.split("o")) #crea una lista, separa en str independientes el dato principal por cada vez que sale el dato que introducimos.