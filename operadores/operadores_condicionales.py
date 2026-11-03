#variable ("algo")

#operador(if) #condicional(*,<,in)
        #accion(hacer algo)
#operador(else) #condicional(*,<,in)
        #accion(hacer algo)

contraseña_almacenada = "santi"
contraseña_escrita = "santiago"

if contraseña_escrita == contraseña_almacenada:
    print("ingresando")
else:
    print("contraseña incorrecta")





ingresos_mensuales = 1800000
gastos_mensuales = 1280000

if ingresos_mensuales >= 2200000:
    print("estas normal")
elif ingresos_mensuales >= 1800000:
    print("tas luchandola")
elif ingresos_mensuales >= 1300000:
    print("ta difiil la cosa")
elif ingresos_mensuales >=2200001:
    print("boff")
else:
    print("tas en la inmunda")





ingresos_mensuales = 1800000
gastos_mensuales = 1280000

if ingresos_mensuales >= 2200000:
    if gastos_mensuales <= 1280000:
        print("estas normal")
elif ingresos_mensuales > 1800000:
    if gastos_mensuales <=1280000:
        print("tas luchandola")
elif ingresos_mensuales > 1300000:
    if gastos_mensuales <=1280000:
        print("ta difiil la cosa")
elif ingresos_mensuales >2200001:
    if gastos_mensuales <=1280000:
        print("boff")
else:
    print("tas en la inmunda")





ingresos_mensuales = 2000000
gastos_mensuales = 1400000

comida = 280000
transporte = 280000
vivienda = 450000
educacion = 350000

if ingresos_mensuales - gastos_mensuales > 900000:
    print("tienes una base de mas de 900 libres")
elif ingresos_mensuales - gastos_mensuales >= 640000:
    print("tienes una base de mas de 600 libres")
elif ingresos_mensuales - gastos_mensuales <= 0:
    print("bro esta en quiebra")
else:
    print("calcula tus ingrsos")
