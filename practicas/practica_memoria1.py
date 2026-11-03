nombres = input("nombres: ")
apellidos = input("apellidos: ")
edad = input("edad: ")
nickname = input("nickname: ")

print("bienvenido " + nickname)
estado = input("como te encuentras hoy?: ")

if "bien" in estado:
    print("me alegro de ecucharlo")
elif "mal" in estado:
    print("no puede ser y eso por q?")
else:
    print("cuentame y eso?")
