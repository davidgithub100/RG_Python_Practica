#reformulacion: int() es una funcion que recibe un dato y lo devuelve como numero entero.
#la variable original se transforma.
#correccion: int() es una funcion que recibe un dato y devuelve un numero entero.
#la variable sigue siendo el valor original, int() crea una copia con valor de numero entero.

#print(int("24"))   # no va arrojar error, es valido para cambiar el tipo de dato y va inprimir 24 como numero entero.

#print(int("24.5")) # en teoria int aun si el valor es float lo vuelve int, en este caso es un str y creo que va ser un error valuerror porque es valido que sea un str pero no es un str numerico porque lleva un .
                    #rectificacion: int() acepta valores float, en este caso es valuerror ya que int() no recive str que no sean numero entero. Para que acepte primero se aplica funcion float() para converit el valor en decimal y luego se aplica int() para cortar el valor decimal y hacerlo entero.

#print(int(24.5))   # en este caso es un type error porque float al ser un valor que lleva . int() no lo puede interpretar por el . 
                    # correccion: int() recibe valores float, corta el valor decimal y deja en eltero tal cual como esta sin aproximar, entonces no arroja error.

print(int("24"))
print(int("24.5"))
print(int(24.5))