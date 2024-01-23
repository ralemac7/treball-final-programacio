import time

print("Dunder Mifflin Paper Company - Gestor de clients")
print(" ")
usuari = str(input("Benvingut! Introdueix el teu nom d'usuari: "))
time.sleep(1)

if usuari == "shudson" or usuari == "amartin":
    contrasenya = int(input("Hola de nou, {usuari}! Introdueix la teva contrasenya: "))
    time.sleep(2)
    if usuari == "shudson" and contrasenya == 103905:
        print(f"Sessió iniciada com a {usuari}. Carregant funcions del departament de compres.")
    elif usuari == "amartin" and contrasenya == 730782:
        print(f"Sessió iniciada com a {usuari}. Carregant funcions del departament de compres.")
    else:
        print("Contrasenya incorrecta. Aturant el programa...")
elif usuari == "dschrute" or usuari == "jhalpert" or usuari == "abernard":
    contrasenya = int(input("Hola de nou, {usuari}! Introdueix la teva contrasenya: "))
    time.sleep(2)
    if usuari == "dschrute" and contrasenya == 817901:
        print(f"Sessió iniciada com a {usuari}. Carregant funcions del departament de vendes.")
    elif usuari == "jhalpert" and contrasenya == 761528:
        print(f"Sessió iniciada com a {usuari}. Carregant funcions del departament de vendes.")
    elif usuari == "abernard" and contrasenya == 918642:
        print(f"Sessió iniciada com a {usuari}. Carregant funcions del departament de vendes.")
    else:
        print("Contrasenya incorrecta. Aturant el programa...")
else:
    print("Usuari no registrat. Aturant el programa...")