import time
import os

# usuaris = {"shudson": 103905, "amartin": 730782, "dschrute": 817901, "jhalpert": 761528, "abernard": 918642}
usuaris = {"shudson": 1, "amartin": 1, "dschrute": 1, "jhalpert": 1, "abernard": 1}
comptes = {"shudson": "compres", "amartin": "compres", "dschrute": "vendes", "jhalpert": "vendes", "abernard": "vendes"}

# Definició de variables
capital = 5000
estocPaper = {"A6": 0, "A5": 0, "A4": 0, "A3": 0, "A2": 0}
estocSobres = {"C6": 0, "C5": 0, "C4": 0, "C3": 0, "C2": 0}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
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
if compte == "compres":
    while True:
        funcioCompres = int(input(f"""Dunder Mifflin Paper Company - Departament de compres ({usuari})
Utilitza el teclat numèric per seleccionar una opció:
    1) Consultar estoc de paper i sobres
    2) Consultar preu de paper i sobres
    2) Consultar compres
    3) Consultar clients (zones)
    4) Comprar paper
    5) Comprar sobres
    6) Consultar capital
    7) Tancar la sessió
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
                print(f"{estocSobres['C1']} paquets de sobres C1")
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
                print(f"{estocPaper['A6']} € per paquet de paper A6")
                print(f"{estocPaper['A5']} € per paquet de paper A5")
                print(f"{estocPaper['A4']} € per paquet de paper A4")
                print(f"{estocPaper['A3']} € per paquet de paper A3")
                print(f"{estocPaper['A2']} € per paquet de paper A2")
                print("")
                print("Tornant al menú prinicipal en 3 segons...")
                time.sleep(3)
            elif opcio == 2:
                print("Mostrant preu de compra de sobres: ")
                print(f"{estocSobres['C6']}€ per paquet de sobres C6")
                print(f"{estocSobres['C5']}€ per paquet de sobres C5")
                print(f"{estocSobres['C4']}€ per paquet de sobres C4")
                print(f"{estocSobres['C3']}€ per paquet de sobres C3")
                print(f"{estocSobres['C2']}€ per paquet de sobres C2")
                print(f"{estocSobres['C1']}€ per paquet de sobres C1")
                print("")
                print("Tornant al menú prinicipal en 3 segons...")
                time.sleep(3)
            else:
                print("Opció incorrecta. Tornant al menu anterior...")
                time.sleep(1)
        elif funcioCompres == 3:
            print("XD")
        elif funcioCompres == 4:
            print("XD")
        elif funcioCompres == 5:
            print("XD")
        elif funcioCompres == 6:
            print("XD")
        elif funcioCompres == 7:
            print("Gràcies per utilitzar el programa. Tancant la sessió...")
            time.sleep(1)
            break
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