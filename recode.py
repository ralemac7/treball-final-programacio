import time
import os

def clear():
    os.system('clear')

comptes = {
    "shudson": {"contrasenya": 1, "carrec": "compres"},
    "amartin": {"contrasenya": 1, "carrec": "compres"},
    "dschrute": {"contrasenya": 1, "carrec": "vendes"},
    "jhalpert": {"contrasenya": 1, "carrec": "vendes"},
    "abernard": {"contrasenya": 1, "carrec": "vendes"},
}

# Definició de variables
capital = 5000
estocPaper = {"A6": 0, "A5": 0, "A4": 0, "A3": 0, "A2": 0}
estocSobres = {"C6": 0, "C5": 0, "C4": 0, "C3": 0, "C2": 0}

proveidors = ["PaperVIP", "ExpressPapereria", "Paper&Co"]
compradorsZona1

# Inici de sessió
print("Dunder Mifflin Paper Company - Gestor de clients")
print(" ")
while True:
    usuari = str(input("Benvingut al programa de gestió de clients. Si us plau, introdueix el teu usuari: "))
    time.sleep(1)
    if usuari in comptes:
        print("Benvingut, " + usuari + ".")
        while True:
            contrasenya = int(input("Si us plau, introdueix la teva contrasenya: "))
            if contrasenya == comptes[usuari]['contrasenya']:
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

if comptes[usuari]['carrec'] == 'compres':
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
            while True
                proveidor = int(input("""A quin proveïdor vols comprar?
    1) PaperVIP
    2) ExpressPapereria
    3) Paper&Co
                                    
    Opció escollida: """))
                if proveidor == 1:
                    nomProveidor = "PaperVIP"
                elif proveidor == 2:
                    nomProveidor = "ExpressPapereria"
                elif proveidor == 3:
                    nomProveidor = "Paper&Co"
                else:
                    print("Opció incorrecta. Tornant al menú principal...")
                    time.sleep(1)
                    break

                opcio = int(input(f"""Realitzar compra a {proveidor}
    Quin paper vols comprar?

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


elif comptes[usuari]['carrec'] == 'vendes':
    print("Vendes")