# Importació de llibreries
import time
import os

# usuaris = {"shudson": 103905, "amartin": 730782, "dschrute": 817901, "jhalpert": 761528, "abernard": 918642}
usuaris = {"shudson": 1, "amartin": 1, "dschrute": 1, "jhalpert": 1, "abernard": 1}
comptes = {"shudson": "compres", "amartin": "compres", "dschrute": "vendes", "jhalpert": "vendes", "abernard": "vendes"}

# Definició de variables
capital = 5000
estocPaper = {"A6": 0, "A5": 0, "A4": 0, "A3": 0, "A2": 0}
estocSobres = {"C6": 0, "C5": 0, "C4": 0, "C3": 0, "C2": 0}

# Neteja de la consola (Windows/Linux)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# def compraPaper(tipus, quantitat, preu)
#    estocPaper[tipus] += quantitat
#    capital -= preu * quantitat
#    print(f"Compra realitzada. El teu capital actual és de {capital}€.")
#    print(" ")
def compraPaper(tipus, quantitat, preu):
    global capital
    if capital >= ((preu * quantitat) * 1.04):
        estocPaper[tipus] += quantitat
        capital -= preu * quantitat
        print(f"Compra realitzada. El teu capital actual és de {capital}€.")
    else:
        print("No tens suficient capital per realitzar aquesta compra.")
        print(f"Necessites {((preu * quantitat) * 1.04) - capital}€ més per realitzar aquesta compra.")
def compraSobres(tipus, quantitat, preu):
    global capital
    if capital >= ((preu * quantitat) * 1.04):
        estocSobres[tipus] += quantitat
        capital -= preu * quantitat
        print(f"Compra realitzada. El teu capital actual és de {capital}€.")
    else:
        print("No tens suficient capital per realitzar aquesta compra.")
        print(f"Necessites {((preu * quantitat) * 1.04) - capital}€ més per realitzar aquesta compra.")
clear()

# Inici de sessió
print("Dunder Mifflin Paper Company - Gestor de clients")
print(" ")
while True:
    usuari = str(input("Benvingut al programa de gestió de clients. Si us plau, introdueix el teu usuari: "))
    time.sleep(1)
    if usuari in usuaris:
        print(" ")
        print("Benvingut, " + usuari + ".")
        print(" ")
        while True:
            contrasenya = int(input("Si us plau, introdueix la teva contrasenya: "))
            if contrasenya == usuaris[usuari]:
                print("Sessió iniciada. Carregant...")
                print(" ")
                time.sleep(2)
                compte = comptes[usuari]
                break
            else:
                print(" ")
                print("Contrasenya incorrecta. Si us plau, introdueix una contrasenya vàlida.")
                print(" ")
                time.sleep(1)
        break
    else:
        print("Usuari incorrecte. Si us plau, introdueix un usuari vàlid.")
        time.sleep(1)

clear()

# Menu del departament de compres
if compte == "compres":
    while True:
        funcioCompres = int(input(f"""Dunder Mifflin Paper Company - Departament de compres ({usuari})
Utilitza el teclat numèric per seleccionar una opció:
    1) Consultar estoc de paper i sobres
    2) Consultar preu de paper i sobres
    3) Consultar capital
    4) Comprar paper
    5) Comprar sobres
    6) Tancar la sessió
Opció escollida: """))
        if funcioCompres == 1:
            opcio = int(input("""Quin estoc vols consultar?
    1) Paper
    2) Sobres
Opció escollida: """))
            if opcio == 1:
                print("Mostrant estoc de paper: ")
                print(f"{estocPaper['A6']} paquets de paper A6")
                print(f"{estocPaper['A5']} paquets de paper A5")
                print(f"{estocPaper['A4']} paquets de paper A4")
                print(f"{estocPaper['A3']} paquets de paper A3")
                print(f"{estocPaper['A2']} paquets de paper A2")
                print("")
                print("Tornant al menú prinicipal en 3 segons...")
                time.sleep(3)
            elif opcio == 2:
                print("Mostrant estoc de sobres: ")
                print(f"{estocSobres['C6']} paquets de sobres C6")
                print(f"{estocSobres['C5']} paquets de sobres C5")
                print(f"{estocSobres['C4']} paquets de sobres C4")
                print(f"{estocSobres['C3']} paquets de sobres C3")
                print(f"{estocSobres['C2']} paquets de sobres C2")
                print("")
                print("Tornant al menú prinicipal en 3 segons...")
                time.sleep(3)
            else:
                print("Opció incorrecta. Tornant al menu anterior...")
                time.sleep(1)
        elif funcioCompres == 2:
            opcio = int(input("""Quin preu vols consultar?
    1) Paper
    2) Sobres
Opció escollida: """))
            if opcio == 1:
                print("Mostrant preu de compra de paper: ")
                print("- Paquet de paper A6 (500 unitats): 18,95€")
                print("- Paquet de paper A5 (500 unitats): 11,34€")
                print("- Paquet de paper A4 (500 unitats): 7,98€")
                print("- OFERTA: 5 paquets paper DIN A4 (500 unitats) - 37,65€")
                print("- Paquet de paper A3 (500 unitats): 7,13€")
                print("- OFERTA: 5 paquets paper DIN A3 (500 unitats) - 58,45€")
                print("- Paquet de paper A2 (500 unitats): 6,45€")
                print("")
                print("Tornant al menú prinicipal en 3 segons...")
                time.sleep(3)
            elif opcio == 2:
                print("Mostrant preu de compra de sobres: ")
                print("- Paquet de sobres C6 (100 unitats): 33,45€")
                print("- Paquet de sobres C5 (100 unitats): 30,58€")
                print("- Paquet de sobres C4 (100 unitats): 24,78€")
                print("- Paquet de sobres C3 (100 unitats): 20,80")
                print("- Paquet de sobres C2 (100 unitats): 16,15€")
                print("")
                print("Tornant al menú prinicipal en 3 segons...")
                time.sleep(3)
            else:
                print("Opció incorrecta. Tornant al menu anterior...")
                time.sleep(1)
        elif funcioCompres == 3:
            print(f"El capital actual de l'empresa és de {capital}€.")
            print(" ")
            print("Tornant al menú prinicipal en 3 segons...")
            time.sleep(3)
        elif funcioCompres == 4:
            opcio = int(input("""Quin paper vols comprar?
1) Paper DIN A6 (500 unitats) - 18,95€
2) Paper DIN A5 (500 unitats) - 11,34€
3) Paper DIN A4 (500 unitats) - 7,98€
4) OFERTA: 5 paquets paper DIN A4 (500 unitats) - 37,65€
5) Paper DIN A3 (500 unitats) - 7,13€
6) OFERTA: 5 paquets paper DIN A3 (500 unitats) - 58,45€
7) Paper DIN A2 (500 unitats) - 6,45€
                              
Per referència, el teu capital actual és de {capital}€.
Per avortar la compra, introdueix 0.
Opció escollida:"""))
            if opcio == 0:
                print("Compra avortada. Tornant al menú principal...")
                time.sleep(1)
            elif opcio == 1:
                compraPaper("A6", int(input("Quants paquets de paper DIN A6 vols comprar? ")), 18.95)
            elif opcio == 2:
                compraPaper("A5", int(input("Quants paquets de paper DIN A5 vols comprar? ")), 11.34)
            elif opcio == 3:
                compraPaper("A4", int(input("Quants paquets de paper DIN A4 vols comprar? ")), 7.98)
            elif opcio == 4:
                quantitat = int(input("Quants ofertes de 5 paquets de paper DIN A4 vols comprar? "))
                if capital >= ((37.65 * quantitat) * 1.04):
                    estocPaper["A4"] += 5 * quantitat
                    capital -= 37.65 * quantitat
                    print(f"Compra realitzada. El teu capital actual és de {capital}€.")
                    print(" ")
            elif opcio == 5:
                compraPaper("A3", int(input("Quants paquets de paper DIN A3 vols comprar? ")), 7.13)
            elif opcio == 6:
                quantitat = int(input("Quants ofertes de 5 paquets de paper DIN A3 vols comprar? "))
                if capital >= ((58.45 * quantitat) * 1.04):
                    estocPaper["A3"] += 5 * quantitat
                    capital -= 58.45 * quantitat
                    print(f"Compra realitzada. El teu capital actual és de {capital}€.")
                    print(" ")
            elif opcio == 7:
                compraPaper("A2", int(input("Quants paquets de paper DIN A2 vols comprar? ")), 6.45)
        elif funcioCompres == 5:
            opcio = int(input(f"""Quins sobres vols comprar?
1) Sobres DIN C6 (100 unitats) - 33,45€
2) Sobres DIN C5 (100 unitats) - 30,58€
3) Sobres DIN C4 (100 unitats) - 24,78€
4) Sobres DIN C3 (100 unitats) - 20,80€
5) Sobres DIN C2 (100 unitats) - 16,15€
                              
Per referència, el teu capital actual és de {capital}€.
Per avortar la compra, introdueix 0.
Opció escollida:"""))
            if opcio == 0:
                print("Compra avortada. Tornant al menú principal...")
                time.sleep(1)
            elif opcio == 1:
                compraSobres("C6", int(input("Quants paquets de sobres DIN C6 vols comprar? ")), 33.45)
            elif opcio == 2:
                compraSobres("C5", int(input("Quants paquets de sobres DIN C5 vols comprar? ")), 30.58)
            elif opcio == 3:
                compraSobres("C4", int(input("Quants paquets de sobres DIN C4 vols comprar? ")), 24.78)
            elif opcio == 4:
                compraSobres("C3", int(input("Quants paquets de sobres DIN C3 vols comprar? ")), 20.80)
            elif opcio == 5:
                compraSobres("C2", int(input("Quants paquets de sobres DIN C2 vols comprar? ")), 16.15)
        elif funcioCompres == 6:
            print("Gràcies per utilitzar el programa. Tancant la sessió...")
            time.sleep(1)
            break
        else:
            print("Opció incorrecta. Si us plau, introdueix una opció vàlida.")
            time.sleep(1)

# Menu del departament de vendes
elif compte == "vendes":
    while True:
        funcio = int(input(f"""Dunder Mifflin Paper Company - Departament de vendes ({usuari})
Utilitza el teclat numèric per seleccionar una opció:
    1) Consultar estoc de paper
    2) Consultar estoc de sobres
    3) Consultar capital
    4) Comprar paper
    5) Comprar sobres
    6) Tancar la sessió
Opció escollida: """))