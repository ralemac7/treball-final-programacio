import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

comptes = {
    "shudson": {"contrasenya": 103905, "carrec": "compres"},
    "amartin": {"contrasenya": 730782, "carrec": "compres"},
    "dschrute": {"contrasenya": 817901, "carrec": "vendes"},
    "jhalpert": {"contrasenya": 761528, "carrec": "vendes"},
    "abernard": {"contrasenya": 918642, "carrec": "vendes"},
}

# Definició de variables
capital = 5000
estocPaper = {"A6": 0, "A5": 0, "A4": 0, "A3": 0, "A2": 0}
estocSobres = {"C6": 0, "C5": 0, "C4": 0, "C3": 0, "C2": 0}

proveidors = {"PaperVIP": 0, "ExpressPapereria": 0, "Paper&Co": 0}
clientsZonaA = {"Naturgraf": 0, "ReciclatPrint": 0, "Fustaprint": 0}
clientsZonaB = {"TecnoGràfic": 0, "EcoArts": 0, "FustaStamp": 0}
clientsZonaC = {"coScript": 0, "SostenPack": 0, "CelluArts": 0}

while True:
    clear()
    print("Dunder Mifflin Paper Company - Gestor de clients")
    print(" ")
    while True:
        usuari = str(input("Benvingut al programa de gestió de clients. Si us plau, inicia la sessió:\nPer a tancar el programa, introdueix 0.\nUsuari: "))
        if usuari == "0":
            print("Gràcies per utilitzar el programa. Aturant...")
            time.sleep(1)
            exit()
        else:
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
        2) Consultar preu de compra paper i sobres
        3) Consultar capital
        4) Gestió de proveïdors (afegir, eliminar o consultar)
        5) Comprar paper
        6) Comprar sobres
        7) Estadístiques de compres
        8) Tancar la sessió
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
                    print("- Paquet de paper A6 (500 unitats): 6,45€")
                    print("- Paquet de paper A5 (500 unitats): 7,13€")
                    print("- Paquet de paper A4 (500 unitats): 7,98€")
                    print("- OFERTA: 5 paquets paper DIN A4 (500 unitats) - 37,65€")
                    print("- Paquet de paper A3 (500 unitats): 11,34€")
                    print("- OFERTA: 5 paquets paper DIN A3 (500 unitats) - 58,45€")
                    print("- Paquet de paper A2 (500 unitats): 18,95€")
                    print("")
                    print("Tornant al menú prinicipal en 3 segons...")
                    time.sleep(3)
                elif opcio == 2:
                    print("Mostrant preu de compra de sobres: ")
                    print("- Paquet de sobres C6 (100 unitats): 16,15€")
                    print("- Paquet de sobres C5 (100 unitats): 20,80€")
                    print("- Paquet de sobres C4 (100 unitats): 24,78€")
                    print("- Paquet de sobres C3 (100 unitats): 30,58€")
                    print("- Paquet de sobres C2 (100 unitats): 33,45€")
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
                while True:
                    opcioGestioProveidors = int(input("""Gestió de proveïdors
        1) Afegir proveïdor nou
        2) Eliminar proveïdor
        3) Consultar llistat de proveïdors
    Per tornar al menú principal, introdueix 0.
    Opció escollida: """))
                    if opcioGestioProveidors == 0:
                        print("Tornant al menú principal...")
                        time.sleep(1)
                        break
                    elif opcioGestioProveidors == 1:
                        proveidorNou = str(input("Introdueix el nom del proveïdor nou: "))
                        proveidors[proveidorNou] = 0
                        print(f"Proveïdor {proveidorNou} afegit correctament.")
                        print(" ")
                    elif opcioGestioProveidors == 2:
                        print("Llistat de proveïdors: ")
                        for proveidor in proveidors:
                            print(f"- {proveidor}")
                        proveidorEliminar = str(input("Introdueix el nom del proveïdor que vols eliminar: "))
                        if proveidorEliminar in proveidors:
                            del proveidors[proveidorEliminar]
                            print(f"Proveïdor {proveidorEliminar} eliminat correctament.")
                            print(" ")
                        else:
                            print("Proveïdor no trobat. Si us plau, introdueix un proveïdor vàlid.")
                            print(" ")
                    elif opcioGestioProveidors == 3:
                        print("Llistat de proveïdors: ")
                        for proveidor in proveidors:
                            print(f"- {proveidor}")
                        print(" ")
                    else:
                        print("Opció incorrecta. Si us plau, introdueix una opció vàlida.")
                        print(" ") 
            elif funcioCompres == 5:            
                while True:
                    print("Compra de paper - Selecció de proveïdor: ")
                    for proveidor in proveidors:
                        print(f"- {proveidor}")
                    while True:
                        proveidorPaper = str(input("Introdueix el nom del proveïdor al que comprar: "))
                        if proveidorPaper in proveidors:
                            print(f"Proveïdor {proveidorPaper} seleccionat correctament.")
                            break
                        else:
                            print("Proveïdor no trobat. Si us plau, introdueix un proveïdor vàlid.")
                            print(" ")
                    opcio = int(input(f"""Quin paper vols comprar?
    1) Paper DIN A6 (500 unitats) - 6,45€
    2) Paper DIN A5 (500 unitats) - 7,13€
    3) Paper DIN A4 (500 unitats) - 7,98€
    4) OFERTA: 5 paquets paper DIN A4 (500 unitats) - 37,65€
    5) Paper DIN A3 (500 unitats) - 11,34€
    6) OFERTA: 5 paquets paper DIN A3 (500 unitats) - 58,45€
    7) Paper DIN A2 (500 unitats) - 18,95€
                                
    Per referència, el capital actual és de {capital}€.
    Per avortar la compra, introdueix 0.
    Opció escollida: """))
                    if opcio == 0:
                        print("Compra avortada. Tornant al menú principal...")
                        time.sleep(1)
                        break
                    elif opcio == 1:
                        while True:
                            quantitat = int(input("Quants paquets de paper DIN A6 vols comprar? "))
                            if (estocPaper['A6'] + quantitat) > 300:
                                print("El límit d'estoc de paper DIN A6 és de 300 paquets.")
                                print(f"L'estoc actual és de {estocPaper['A6']} paquets.")
                                print(" ")
                                print(f"Introdueix una quantitat vàlida (1-{(300 - estocPaper['A6'])}).")
                            else:
                                break
                        if capital >= (6.45 * quantitat):
                            estocPaper['A6'] += quantitat
                            if quantitat >= 4:
                                capital -= (6.45 * quantitat) * 0.97 * 1.04
                                proveidors[proveidorPaper] += (6.45 * quantitat) * 0.97
                            else:
                                capital -= 6.45 * quantitat * 1.04
                                proveidors[proveidorPaper] += 6.45 * quantitat
                            print(f"Compra de {quantitat} paquets de paper DIN A6 realitzada correctament.")
                            print(f"El capital actual és de {capital}€.")
                            print(" ")
                        else:
                            print("No tens prou capital per realitzar aquesta compra.")
                            print(" ")
                        break
                    elif opcio == 2:
                        while True:
                            quantitat = int(input("Quants paquets de paper DIN A5 vols comprar? "))
                            if (estocPaper['A5'] + quantitat) > 150:
                                print("El límit d'estoc de paper DIN A5 és de 150 paquets.")
                                print(f"L'estoc actual és de {estocPaper['A5']} paquets.")
                                print(" ")
                                print(f"Introdueix una quantitat vàlida (1-{(150 - estocPaper['A5'])}).")
                            else:
                                break
                        if capital >= (7.13 * quantitat):
                            estocPaper['A5'] += quantitat
                            if quantitat >= 4:
                                capital -= (7.13 * quantitat) * 0.96 * 1.04
                                proveidors[proveidorPaper] += (7.13 * quantitat) * 0.96
                            else:
                                capital -= 7.13 * quantitat * 1.04
                                proveidors[proveidorPaper] += 7.13 * quantitat
                            print(f"Compra de {quantitat} paquets de paper DIN A5 realitzada correctament.")
                            print(f"El capital actual és de {capital}€.")
                            print(" ")
                        else:
                            print("No tens prou capital per realitzar aquesta compra.")
                            print(" ")
                        break
                    elif opcio == 3:
                        while True:
                            quantitat = int(input("Quants paquets de paper DIN A4 vols comprar? "))
                            if (estocPaper['A4'] + quantitat) > 400:
                                print("El límit d'estoc de paper DIN A4 és de 400 paquets.")
                                print(f"L'estoc actual és de {estocPaper['A4']} paquets.")
                                print(" ")
                                print(f"Introdueix una quantitat vàlida (1-{(400 - estocPaper['A4'])}).")
                            else:
                                break
                        if capital >= (7.98 * quantitat):
                            estocPaper['A4'] += quantitat
                            if quantitat >= 4:
                                capital -= (7.98 * quantitat) * 0.95 * 1.04
                                proveidors[proveidorPaper] += (6.45 * quantitat) * 0.95
                            else:
                                capital -= 7.98 * quantitat * 1.04
                                proveidors[proveidorPaper] += 7.98 * quantitat
                            print(f"Compra de {quantitat} paquets de paper DIN A4 realitzada correctament.")
                            print(f"El capital actual és de {capital}€.")
                            print(" ")
                        else:
                            print("No tens prou capital per realitzar aquesta compra.")
                            print(" ")
                        break
                    elif opcio == 4:
                        while True:
                            quantitat = int(input("Quants lots de 5 paquets de paper DIN A4 vols comprar? "))
                            if (estocPaper['A4'] + (5 * quantitat)) > 400:
                                print("El límit d'estoc de paper DIN A4 és de 400 paquets.")
                                print(f"L'estoc actual és de {estocPaper['A4']} paquets.")
                                print(" ")
                                print(f"Introdueix una quantitat vàlida (1-{(400 - estocPaper['A4']) / 5}).")
                            else:
                                break
                        if capital >= (37.65 * quantitat):
                            estocPaper['A4'] += 500 * (quantitat *5)
                            if quantitat >= 4:
                                capital -= (37.65 * quantitat) * 0.98 * 1.04
                                proveidors[proveidorPaper] += (37.65 * quantitat) * 0.98
                            else:
                                capital -= 37.65 * quantitat * 1.04
                                proveidors[proveidorPaper] += 37.65 * quantitat
                            print(f"Compra de {quantitat} lots de 5 paquets de paper DIN A4 realitzada correctament.")
                            print(f"El capital actual és de {capital}€.")
                            print(" ")
                        else:
                            print("No tens prou capital per realitzar aquesta compra.")
                            print(" ")
                        break
                    elif opcio == 5:
                        while True:
                            quantitat = int(input("Quants paquets de paper DIN A3 vols comprar? "))
                            if (estocPaper['A3'] + quantitat) > 150:
                                print("El límit d'estoc de paper DIN A3 és de 150 paquets.")
                                print(f"L'estoc actual és de {estocPaper['A3']} paquets.")
                                print(" ")
                                print(f"Introdueix una quantitat vàlida (1-{(150 - estocPaper['A3'])}).")
                            else:
                                break
                        if capital >= (11.34 * quantitat):
                            estocPaper['A3'] += quantitat
                            if quantitat >= 4:
                                capital -= (11.34 * quantitat) * 0.94 * 1.04
                                proveidors[proveidorPaper] += (11.34 * quantitat) * 0.94
                            else:
                                capital -= 11.34 * quantitat * 1.04
                                proveidors[proveidorPaper] += 11.34 * quantitat
                            print(f"Compra de {quantitat} paquets de paper DIN A3 realitzada correctament.")
                            print(f"El capital actual és de {capital}€.")
                            print(" ")
                        else:
                            print("No tens prou capital per realitzar aquesta compra.")
                            print(" ")
                        break
                    elif opcio == 6:
                        while True:
                            quantitat = int(input("Quants lots de 5 paquets de paper DIN A3 vols comprar? "))
                            if (estocPaper['A3'] + (5 * quantitat)) > 150:
                                print("El límit d'estoc de paper DIN A3 és de 150 paquets.")
                                print(f"L'estoc actual és de {estocPaper['A3']} paquets.")
                                print(" ")
                                print(f"Introdueix una quantitat vàlida (1-{(150 - estocPaper['A3']) / 5}).")
                            else:
                                break
                        if capital >= (58.45 * quantitat):
                            estocPaper['A3'] += 500 * (quantitat *5)
                            if quantitat >= 4:
                                capital -= (58.45 * quantitat) * 0.97 * 1.04
                                proveidors[proveidorPaper] += (37.65 * quantitat) * 0.97
                            else:
                                capital -= 58.45 * quantitat * 1.04
                                proveidors[proveidorPaper] += 58.45 * quantitat
                            print(f"Compra de {quantitat} lots de 5 paquets de paper DIN A3 realitzada correctament.")
                            print(f"El capital actual és de {capital}€.")
                            print(" ")
                        else:
                            print("No tens prou capital per realitzar aquesta compra.")
                            print(" ")
                        break
                    elif opcio == 7:
                        while True:
                            quantitat = int(input("Quants paquets de paper DIN A2 vols comprar? "))
                            if (estocPaper['A2'] + quantitat) > 100:
                                print("El límit d'estoc de paper DIN A2 és de 100 paquets.")
                                print(f"L'estoc actual és de {estocPaper['A2']} paquets.")
                                print(" ")
                                print(f"Introdueix una quantitat vàlida (1-{(100 - estocPaper['A2'])}).")
                            else:
                                break
                        if capital >= (18.95 * quantitat):
                            estocPaper['A2'] += quantitat
                            if quantitat >= 4:
                                capital -= (18.95 * quantitat) * 0.93 * 1.04
                                proveidors[proveidorPaper] += (18.95 * quantitat) * 0.93
                            else:
                                capital -= 18.95 * quantitat * 1.04
                                proveidors[proveidorPaper] += 18.95 * quantitat
                            print(f"Compra de {quantitat} paquets de paper DIN A2 realitzada correctament.")
                            print(f"El capital actual és de {capital}€.")
                            print(" ")
                        else:
                            print("No tens prou capital per realitzar aquesta compra.")
                            print(" ")
                    else:
                        print("Opció incorrecta. Si us plau, introdueix una opció vàlida.")
                        print(" ")
                    break
            elif funcioCompres == 6:
                while True:
                    print("Compra de sobres - Selecció de proveïdor: ")
                    for proveidor in proveidors:
                        print(f"- {proveidor}")
                    while True:
                        proveidorSobres = str(input("Introdueix el nom del proveïdor al que comprar: "))
                        if proveidorSobres in proveidors:
                            print(f"Proveïdor {proveidorPaper} seleccionat correctament.")
                            break
                        else:
                            print("Proveïdor no trobat. Si us plau, introdueix un proveïdor vàlid.")
                            print(" ")
                    opcio = int(input(f"""Quins sobres vols comprar?
    1) Sobres DIN C6 (100 unitats) - 33,45€
    2) Sobres DIN C5 (100 unitats) - 30,58€
    3) Sobres DIN C4 (100 unitats) - 24,78€
    4) Sobres DIN C3 (100 unitats) - 20,80€
    5) Sobres DIN C2 (100 unitats) - 16,15€
                                
    Per referència, el teu capital actual és de {capital}€.
    Per avortar la compra, introdueix 0.
    Opció escollida: """))
                    if opcio == 0:
                        print("Compra avortada. Tornant al menú principal...")
                        time.sleep(1)
                        break
                    elif opcio == 1:
                        while True:
                            quantitat = int(input("Quants paquets de sobres DIN C6 vols comprar? "))
                            if (estocSobres['C6'] + quantitat) > 300:
                                print("El límit d'estoc de sobres DIN C6 és de 300 paquets.")
                                print(f"L'estoc actual és de {estocSobres['C6']} paquets.")
                                print(" ")
                                print(f"Introdueix una quantitat vàlida (1-{(300 - estocSobres['C6'])}).")
                            else:
                                break
                        if capital >= (33.45 * quantitat):
                            estocSobres['C6'] += quantitat
                            if quantitat >= 4:
                                capital -= (33.45 * quantitat) * 0.97 * 1.04
                                proveidors[proveidorSobres] += (33.45 * quantitat) * 0.97
                            else:
                                capital -= 33.45 * quantitat * 1.04
                                proveidors[proveidorSobres] += 33.45 * quantitat
                            print(f"Compra de {quantitat} paquets de sobres DIN C6 realitzada correctament.")
                            print(f"El capital actual és de {capital}€.")
                            print(" ")
                        else:
                            print("No tens prou capital per realitzar aquesta compra.")
                            print(" ")
                        break
                    elif opcio == 2:
                        while True:
                            quantitat = int(input("Quants paquets de sobres DIN C5 vols comprar? "))
                            if (estocSobres['C5'] + quantitat) > 150:
                                print("El límit d'estoc de sobres DIN C5 és de 150 paquets.")
                                print(f"L'estoc actual és de {estocSobres['C5']} paquets.")
                                print(" ")
                                print(f"Introdueix una quantitat vàlida (1-{(150 - estocSobres['C5'])}).")
                            else:
                                break
                        if capital >= (30.58 * quantitat):
                            estocSobres['C5'] += quantitat
                            if quantitat >= 4:
                                capital -= (30.58 * quantitat) * 0.96 * 1.04
                                proveidors[proveidorSobres] += (30.58 * quantitat) * 0.96
                            else:
                                capital -= 30.58 * quantitat * 1.04
                                proveidors[proveidorSobres] += 30.58 * quantitat
                            print(f"Compra de {quantitat} paquets de sobres DIN C5 realitzada correctament.")
                            print(f"El capital actual és de {capital}€.")
                            print(" ")
                        else:
                            print("No tens prou capital per realitzar aquesta compra.")
                            print(" ")
                        break
                    elif opcio == 3:
                        while True:
                            quantitat = int(input("Quants paquets de sobres DIN C4 vols comprar? "))
                            if (estocSobres['C4'] + quantitat) > 400:
                                print("El límit d'estoc de sobres DIN C4 és de 400 paquets.")
                                print(f"L'estoc actual és de {estocSobres['C4']} paquets.")
                                print(" ")
                                print(f"Introdueix una quantitat vàlida (1-{(400 - estocSobres['C4'])}).")
                            else:
                                break
                        if capital >= (24.78 * quantitat):
                            estocSobres['C4'] += quantitat
                            if quantitat >= 4:
                                capital -= (24.78 * quantitat) * 0.95 * 1.04
                                proveidors[proveidorSobres] += (24.78 * quantitat) * 0.95
                            else:
                                capital -= 24.78 * quantitat * 1.04
                                proveidors[proveidorSobres] += 24.78 * quantitat
                            print(f"Compra de {quantitat} paquets de sobres DIN C4 realitzada correctament.")
                            print(f"El capital actual és de {capital}€.")
                            print(" ")
                        else:
                            print("No tens prou capital per realitzar aquesta compra.")
                            print(" ")
                        break
                    elif opcio == 4:
                        while True:
                            quantitat = int(input("Quants paquets de sobres DIN C3 vols comprar? "))
                            if (estocSobres['C3'] + quantitat) > 300:
                                print("El límit d'estoc de sobres DIN C3 és de 300 paquets.")
                                print(f"L'estoc actual és de {estocSobres['C3']} paquets.")
                                print(" ")
                                print(f"Introdueix una quantitat vàlida (1-{(300 - estocSobres['C3'])}).")
                            else:
                                break
                        if capital >= (20.80 * quantitat):
                            estocSobres['C3'] += quantitat
                            if quantitat >= 4:
                                capital -= (20.80 * quantitat) * 0.94 * 1.04
                                proveidors[proveidorSobres] += (20.80 * quantitat) * 0.94
                            else:
                                capital -= 20.80 * quantitat * 1.04
                                proveidors[proveidorSobres] += 20.80 * quantitat
                            print(f"Compra de {quantitat} paquets de sobres DIN C3 realitzada correctament.")
                            print(f"El capital actual és de {capital}€.")
                            print(" ")
                        else:
                            print("No tens prou capital per realitzar aquesta compra.")
                            print(" ")
                        break
                    elif opcio == 5:
                        while True:
                            quantitat = int(input("Quants paquets de sobres DIN C2 vols comprar? "))
                            if (estocSobres['C2'] + quantitat) > 100:
                                print("El límit d'estoc de sobres DIN C2 és de 100 paquets.")
                                print(f"L'estoc actual és de {estocSobres['C2']} paquets.")
                                print(" ")
                                print(f"Introdueix una quantitat vàlida (1-{(100 - estocSobres['C2'])}).")
                            else:
                                break
                        if capital >= (16.15 * quantitat):
                            estocSobres['C2'] += quantitat
                            if quantitat >= 4:
                                capital -= (16.15 * quantitat) * 0.93 * 1.04
                                proveidors[proveidorSobres] += (16.15 * quantitat) * 0.93
                            else:
                                capital -= 16.15 * quantitat * 1.04
                                proveidors[proveidorSobres] += 16.15 * quantitat
                            print(f"Compra de {quantitat} paquets de sobres DIN C2 realitzada correctament.")
                            print(f"El capital actual és de {capital}€.")
                            print(" ")
                        else:
                            print("No tens prou capital per realitzar aquesta compra.")
                            print(" ")
                        break
                    else:
                        print("Opció incorrecta. Si us plau, introdueix una opció vàlida.")
                        print(" ")
            elif funcioCompres == 7:
                print("Mostrant quantitat d'€ invertits en paper/sobres per proveïdor: ")
                for proveidor in proveidors:
                    print(f"- {proveidor}: {round(proveidors[proveidor], 2)}€")
                print(" ")
                print("Torna al menú principal en 3 segons...")
                time.sleep(3)
            elif funcioCompres == 8:
                print("Gràcies per utilitzar el programa. Tancant la sessió...")
                time.sleep(1)
                break
            else:
                print("Opció incorrecta. Si us plau, introdueix una opció vàlida.")
                time.sleep(1)

    elif comptes[usuari]['carrec'] == 'vendes':
        while True:
            funcioVendes = int(input(f"""Dunder Mifflin Paper Company - Departament de vendes ({usuari})
    Utilitza el teclat numèric per seleccionar una opció:
        1) Consultar estoc de paper i sobres
        2) Consultar preu de venda de paper i sobres
        3) Consultar capital
        4) Gestió de clients (afegir, eliminar o consultar)
        5) Vendre paper
        6) Vendre sobres
        7) Estadístiques de vendes
        8) Tancar la sessió
    Opció escollida: """))
            if funcioVendes == 1:
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
            elif funcioVendes == 2:
                opcio = int(input("""Quin preu vols consultar?
        1) Paper
        2) Sobres
        3) Enviament
    Opció escollida: """))
                if opcio == 1:
                    print("Mostrant preu de venda de paper: ")
                    print("- Paquet de paper A6 (500 unitats): 7,35€")
                    print("- Paquet de paper A5 (500 unitats): 8,10€")
                    print("- Paquet de paper A4 (500 unitats): 9,45€")
                    print("- OFERTA: 5 paquets paper DIN A4 (500 unitats) - 42,95€")
                    print("- Paquet de paper A3 (500 unitats): 13,25€")
                    print("- OFERTA: 5 paquets paper DIN A3 (500 unitats) - 63,95€")
                    print("- Paquet de paper A2 (500 unitats): 24,15€")
                    print("")
                    print("Tornant al menú prinicipal en 3 segons...")
                    time.sleep(3)
                elif opcio == 2:
                    print("Mostrant preu de venda de sobres: ")
                    print("- Paquet de sobres C6 (100 unitats): 17.15€")
                    print("- Paquet de sobres C5 (100 unitats): 22,95€")
                    print("- Paquet de sobres C4 (100 unitats): 26,74€")
                    print("- Paquet de sobres C3 (100 unitats): 32,68€")
                    print("- Paquet de sobres C2 (100 unitats): 35,45€")
                    print("")
                    print("Tornant al menú prinicipal en 3 segons...")
                    time.sleep(3)
                elif opcio == 3:
                    print("Mostrant tarifes d'enviament: ")
                    print("- Factures de 0 a 499€: 19,95€")
                    print("- Factures de 500 a 999€: 9,95€")
                    print("- Factures de 1000€ o més: GRATIS")
                    print("")
                    print("Tornant al menú prinicipal en 3 segons...")
                    time.sleep(3)
                else:
                    print("Opció incorrecta. Tornant al menu anterior...")
                    time.sleep(1)
            elif funcioVendes == 3:
                print(f"El capital actual de l'empresa és de {capital}€.")
                print(" ")
                print("Tornant al menú prinicipal en 3 segons...")
                time.sleep(3)
            elif funcioVendes == 4:
                while True:
                    opcioGestioClients = int(input("""Gestió de clients
    1) Afegir client nou
    2) Eliminar client
    3) Consultar llistat de clients
    
    Per tornar al menú principal, introdueix 0.
    Opció escollida: """))
                    if opcioGestioClients == 0:
                        print("Tornant al menú principal...")
                        time.sleep(1)
                        break
                    elif opcioGestioClients == 1:
                        zonaClient = int(input("""A quina zona vols afegir al client?
    1) Zona A
    2) Zona B
    3) Zona C
    
    Per avortar l'acció, introdueix 0.
    Opció escollida: """))
                        if zonaClient == 0:
                            print("Acció avortada. Tornant al menú principal...")
                            time.sleep(1)
                            break
                        elif zonaClient == 1:
                            clientNou = str(input("Introdueix el nom del client nou: "))
                            clientsZonaA[clientNou] = 0
                            print(f"Client {clientNou} afegit correctament a la zona A.")
                            print(" ")
                        elif zonaClient == 2:
                            clientNou = str(input("Introdueix el nom del client nou: "))
                            clientsZonaB[clientNou] = 0
                            print(f"Client {clientNou} afegit correctament a la zona B.")
                            print(" ")
                        elif zonaClient == 3:
                            clientNou = str(input("Introdueix el nom del client nou: "))
                            clientsZonaC[clientNou] = 0
                            print(f"Client {clientNou} afegit correctament a la zona C.")
                            print(" ")
                        else:
                            print("Zona invàlida. Tornant al menu anterior...")
                            time.sleep(1)
                    elif opcioGestioClients == 2:
                        print("Llistat de clients: ")
                        print(f"Zona A: {', '.join(clientsZonaA)}")
                        print(f"Zona B: {', '.join(clientsZonaB)}")
                        print(f"Zona C: {', '.join(clientsZonaC)}")
                        print(" ")
                        zonaClient = int(input("""De quina zona vols eliminar un client?
    1) Zona A
    2) Zona B
    3) Zona C
    
    Per avortar l'acció, introdueix 0.
    Opció escollida: """))
                        if zonaClient == 0:
                            print("Acció avortada. Tornant al menú principal...")
                            time.sleep(1)
                            break
                        elif zonaClient == 1:
                            clientEliminar = str(input("Introdueix el nom del client que vols eliminar: "))
                            if clientEliminar in clientsZonaA:
                                del clientsZonaA[clientEliminar]
                                print(f"Client {clientEliminar} eliminat correctament de la zona A.")
                                print(" ")
                            else:
                                print("Client no trobat. Si us plau, introdueix un client vàlid.")
                                print(" ")
                        elif zonaClient == 2:
                            clientEliminar = str(input("Introdueix el nom del client que vols eliminar: "))
                            if clientEliminar in clientsZonaB:
                                del clientsZonaB[clientEliminar]
                                print(f"Client {clientEliminar} eliminat correctament de la zona B.")
                                print(" ")
                            else:
                                print("Client no trobat. Si us plau, introdueix un client vàlid.")
                                print(" ")
                        elif zonaClient == 3:
                            clientEliminar = str(input("Introdueix el nom del client que vols eliminar: "))
                            if clientEliminar in clientsZonaC:
                                del clientsZonaC[clientEliminar]
                                print(f"Client {clientEliminar} eliminat correctament de la zona C.")
                                print(" ")
                            else:
                                print("Client no trobat. Si us plau, introdueix un client vàlid.")
                                print(" ")
                        else:
                            print("Zona invàlida. Tornant al menu anterior...")
                            time.sleep(1)
                    elif opcioGestioClients == 3:
                        print("Llistat de clients: ")
                        print(f"Zona A: {', '.join(clientsZonaA)}")
                        print(f"Zona B: {', '.join(clientsZonaB)}")
                        print(f"Zona C: {', '.join(clientsZonaC)}")
                        print(" ")
                        print("Tornant al menú principal en 3 segons...")
                        time.sleep(3)
                    else:
                        print("Opció incorrecta. Si us plau, introdueix una opció vàlida.")
                        print(" ")
            elif funcioVendes == 5:
                print("Venda de paper - Selecció de client: ")
                zona = int(input("""A quina zona pertany el client?
    1) Zona A
    2) Zona B
    3) Zona C
    
    Per avortar la venda, introdueix 0.
    Opció escollida: """))
                if zona == 0:
                    print("Venda avortada. Tornant al menú principal...")
                    time.sleep(1)
                    break
                elif zona == 1:
                    zonaClient == clientsZonaA
                    print("Llistat de clients de la zona A: ")
                    print(f"{', '.join(clientsZonaA)}")
                    client = str(input("Introdueix el nom del client: "))
                    if client in clientsZonaA:
                        print(f"Client {client} seleccionat correctament.")
                    else:
                        print("Client no trobat. Si us plau, introdueix un client vàlid.")
                        print(" ")
                elif zona == 2:
                    zonaClient == clientsZonaB
                    print("Llistat de clients de la zona B: ")
                    print(f"{', '.join(clientsZonaB)}")
                    client = str(input("Introdueix el nom del client: "))
                    if client in clientsZonaB:
                        print(f"Client {client} seleccionat correctament.")
                    else:
                        print("Client no trobat. Si us plau, introdueix un client vàlid.")
                        print(" ")
                elif zona == 3:
                    zonaClient == clientsZonaC
                    print("Llistat de clients de la zona C: ")
                    print(f"{', '.join(clientsZonaC)}")
                    client = str(input("Introdueix el nom del client: "))
                    if client in clientsZonaC:
                        print(f"Client {client} seleccionat correctament.")
                    else:
                        print("Client no trobat. Si us plau, introdueix un client vàlid.")
                        print(" ")
                else:
                    print("Zona invàlida. Tornant al menu anterior...")
                    time.sleep(1)
                    break
                print("Opcions de compra de paper:")
                while True:
                    productesComprar = 0
                    aPagar = []
                    opcio = int(input(f"""Quin paper vols comprar?
    1) Paper DIN A6 (500 unitats) - 7,35€
    2) Paper DIN A5 (500 unitats) - 8,10€
    3) Paper DIN A4 (500 unitats) - 9,45€
    4) OFERTA: 5 paquets paper DIN A4 (500 unitats) - 42,95€
    5) Paper DIN A3 (500 unitats) - 13,25€
    6) OFERTA: 5 paquets paper DIN A3 (500 unitats) - 63,95€
    7) Paper DIN A2 (500 unitats) - 24,15€
    
    Si no vols comprar més, introdueix 0.
    Opció escollida: """))
                    if opcio == 0:
                        print("S'ha aturat la selecció de compres.")
                        if productesComprar == 0:
                            print("No s'ha seleccionat cap producte. Tornant al menú principal...")
                            time.sleep(1)
                            break
                        else:
                            print(f"S'han seleccionat {productesComprar} diferents productes.")
                            print(f"El total a pagar dels productes és de {sum(aPagar)}€.")
                            if sum(aPagar) > 0 and sum(aPagar) < 500:
                                print("El client haurá de pagar 19,95€ d'enviament.")
                                preuEnviament = 19.95
                            elif sum(aPagar) >= 500 and sum(aPagar) < 1000:
                                print("El client haurá de pagar 9,95€ d'enviament.")
                                preuEnviament = 9.95
                            elif sum(aPagar) >= 1000:
                                print("El client no haurá de pagar res per l'enviament.")
                                preuEnviament = 0
                            totalIva = (sum(aPagar) + preuEnviament * 1.04)
                            capital += totalIva
                            print(f"El total a pagar per {client} dels productes amb IVA i enviament és de {totalIva}€.")
                    elif opcio == 1:
                        quantitat = int(input("Quants paquets de paper DIN A6 es vendran? "))
                        if (estocPaper['A6'] - quantitat) > 60:
                            estocPaper['A6'] -= quantitat
                            productesComprar += 1
                            if quantitat >= 4:
                                {zonaClient}[client] += 7.35 * quantitat * 0.97
                                aPagar.append(7.35 * quantitat * 0.97)
                            else:
                                {zonaClient}[client] += 7.35 * quantitat
                                aPagar.append(7.35 * quantitat)
                            print(f"Venda de {quantitat} paquets de paper DIN A6 realitzada correctament.")
                            print(" ")
                        else:
                            print("No hi ha prou estoc per realitzar aquesta compra.")
                            print(" ")
                    elif opcio == 2:
                        quantitat = int(input("Quants paquets de paper DIN A5 es vendran? "))
                        if (estocPaper['A5'] - quantitat) > 50:
                            estocPaper['A5'] -= quantitat
                            productesComprar += 1
                            if quantitat >= 4:
                                {zonaClient}[client] += 8.10 * quantitat * 0.96
                                aPagar.append(8.10 * quantitat * 0.96)
                            else:
                                {zonaClient}[client] += 8.10 * quantitat
                                aPagar.append(8.10 * quantitat)
                            print(f"Compra de {quantitat} paquets de paper DIN A5 realitzada correctament.")
                            print(" ")
                        else:
                            print("No hi ha prou estoc per realitzar aquesta compra.")
                            print(" ")
                    elif opcio == 3:
                        quantitat = int(input("Quants paquets de paper DIN A4 es vendran? "))
                        if (estocPaper['A4'] - quantitat) > 100:
                            estocPaper['A4'] -= quantitat
                            productesComprar += 1
                            if quantitat >= 4:
                                {zonaClient}[client] += 9.45 * quantitat * 0.95
                                aPagar.append(9.45 * quantitat * 0.95)
                            else:
                                {zonaClient}[client] += 9.45 * quantitat
                                aPagar.append(9.45 * quantitat)
                            print(f"Compra de {quantitat} paquets de paper DIN A4 realitzada correctament.")
                            print(" ")
                        else:
                            print("No hi ha prou estoc per realitzar aquesta compra.")
                            print(" ")
                    elif opcio == 4:
                        quantitat = int(input("Quants lots de 5 paquets de paper DIN A4 es vendran? "))
                        if (estocPaper['A4'] - (5 * quantitat)) > 100:
                            estocPaper['A4'] -= 5 * quantitat
                            productesComprar += 1
                            if quantitat >= 4:
                                {zonaClient}[client] += 42.95 * quantitat * 0.98
                                aPagar.append(42.95 * quantitat * 0.98)
                            else:
                                {zonaClient}[client] += 42.95 * quantitat
                                aPagar.append(42.95 * quantitat)
                            print(f"Compra de {quantitat} lots de 5 paquets de paper DIN A4 realitzada correctament.")
                            print(" ")
                        else:
                            print("No hi ha prou estoc per realitzar aquesta compra.")
                            print(" ")
                    elif opcio == 5:
                        quantitat = int(input("Quants paquets de paper DIN A3 es vendran? "))
                        if (estocPaper['A3'] - quantitat) > 30:
                            estocPaper['A3'] -= quantitat
                            productesComprar += 1
                            if quantitat >= 4:
                                {zonaClient}[client] += 13.25 * quantitat * 0.94
                                aPagar.append(13.25 * quantitat * 0.94)
                            else:
                                {zonaClient}[client] += 13.25 * quantitat
                                aPagar.append(13.25 * quantitat)
                            print(f"Compra de {quantitat} paquets de paper DIN A3 realitzada correctament.")
                            print(" ")
                        else:
                            print("No hi ha prou estoc per realitzar aquesta compra.")
                            print(" ")
                    elif opcio == 6:
                        quantitat = int(input("Quants lots de 5 paquets de paper DIN A3 es vendran? "))
                        if (estocPaper['A3'] - (5 * quantitat)) > 30:
                            estocPaper['A3'] -= 5 * quantitat
                            productesComprar += 1
                            if quantitat >= 4:
                                {zonaClient}[client] += 63.95 * quantitat * 0.97
                                aPagar.append(63.95 * quantitat * 0.97)
                            else:
                                {zonaClient}[client] += 63.95 * quantitat
                                aPagar.append(63.95 * quantitat)
                            print(f"Compra de {quantitat} lots de 5 paquets de paper DIN A3 realitzada correctament.")
                            print(" ")
                        else:
                            print("No hi ha prou estoc per realitzar aquesta compra.")
                            print(" ")
                    elif opcio == 7:
                        quantitat = int(input("Quants paquets de paper DIN A2 es vendran? "))
                        if (estocPaper['A2'] - quantitat) > 20:
                            estocPaper['A2'] -= quantitat
                            productesComprar += 1
                            if quantitat >= 4:
                                {zonaClient}[client] += 24.15 * quantitat * 0.93
                                aPagar.append(24.15 * quantitat * 0.93)
                            else:
                                {zonaClient}[client] += 24.15 * quantitat
                                aPagar.append(24.15 * quantitat)
                            print(f"Compra de {quantitat} paquets de paper DIN A2 realitzada correctament.")
                            print(" ")
                        else:
                            print("No hi ha prou estoc per realitzar aquesta compra.")
                            print(" ")
                    else:
                        print("Opció incorrecta. Si us plau, introdueix una opció vàlida.")
                        print(" ")
            elif funcioVendes == 6:
                print("Venda de sobres - Selecció de client: ")
                zona = int(input("""A quina zona pertany el client?
    1) Zona A
    2) Zona B
    3) Zona C
    
    Per avortar la venda, introdueix 0.
    Opció escollida: """))
                if zona == 0:
                    print("Venda avortada. Tornant al menú principal...")
                    time.sleep(1)
                    break
                elif zona == 1:
                    zonaClient == clientsZonaA
                    print("Llistat de clients de la zona A: ")
                    print(f"{', '.join(clientsZonaA)}")
                    client = str(input("Introdueix el nom del client: "))
                    if client in clientsZonaA:
                        print(f"Client {client} seleccionat correctament.")
                    else:
                        print("Client no trobat. Si us plau, introdueix un client vàlid.")
                        print(" ")
                elif zona == 2:
                    zonaClient == clientsZonaB
                    print("Llistat de clients de la zona B: ")
                    print(f"{', '.join(clientsZonaB)}")
                    client = str(input("Introdueix el nom del client: "))
                    if client in clientsZonaB:
                        print(f"Client {client} seleccionat correctament.")
                    else:
                        print("Client no trobat. Si us plau, introdueix un client vàlid.")
                        print(" ")
                elif zona == 3:
                    zonaClient == clientsZonaC
                    print("Llistat de clients de la zona C: ")
                    print(f"{', '.join(clientsZonaC)}")
                    client = str(input("Introdueix el nom del client: "))
                    if client in clientsZonaC:
                        print(f"Client {client} seleccionat correctament.")
                    else:
                        print("Client no trobat. Si us plau, introdueix un client vàlid.")
                        print(" ")
                else:
                    print("Zona invàlida. Tornant al menu anterior...")
                    time.sleep(1)
                    break
                print("Opcions de compra de sobres:")
                while True:
                    productesComprar = 0
                    aPagar = []
                    opcio = int(input(f"""Quins sobres vols comprar?
    1) Sobres DIN C6 (100 unitats) - 17,15€
    2) Sobres DIN C5 (100 unitats) - 22,95€
    3) Sobres DIN C4 (100 unitats) - 26,74€
    4) Sobres DIN C3 (100 unitats) - 32,68€
    5) Sobres DIN C2 (100 unitats) - 35,45€
    
    Si no vols comprar més, introdueix 0.
    Opció escollida: """))
                    if opcio == 0:
                        print("S'ha aturat la selecció de compres.")
                        if productesComprar == 0:
                            print("No s'ha seleccionat cap producte. Tornant al menú principal...")
                            time.sleep(1)
                            break
                        else:
                            print(f"S'han seleccionat {productesComprar} diferents productes.")
                            print(f"El total a pagar dels productes és de {sum(aPagar)}€.")
                            if sum(aPagar) > 0 and sum(aPagar) < 500:
                                print("El client haurá de pagar 19,95€ d'enviament.")
                                preuEnviament = 19.95
                            elif sum(aPagar) >= 500 and sum(aPagar) < 1000:
                                print("El client haurá de pagar 9,95€ d'enviament.")
                                preuEnviament = 9.95
                            elif sum(aPagar) >= 1000:
                                print("El client no haurá de pagar res per l'enviament.")
                                preuEnviament = 0
                            totalIva = (sum(aPagar) + preuEnviament * 1.04)
                            capital += totalIva
                            print(f"El total a pagar per {client} dels productes amb IVA i enviament és de {totalIva}€.")
                    elif opcio == 1:
                        quantitat = int(input("Quants paquets de sobres DIN C6 es vendran? "))
                        if (estocSobres['C6'] - quantitat) > 100:
                            estocSobres['C6'] -= quantitat
                            productesComprar += 1
                            if quantitat >= 4:
                                {zonaClient}[client] += 17.15 * quantitat * 0.97
                                aPagar.append(17.15 * quantitat * 0.97)
                            else:
                                {zonaClient}[client] += 17.15 * quantitat
                                aPagar.append(17.15 * quantitat)
                            print(f"Venda de {quantitat} paquets de sobres DIN C6 realitzada correctament.")
                            print(" ")
                        else:
                            print("No hi ha prou estoc per realitzar aquesta compra.")
                            print(" ")
                    elif opcio == 2:
                        quantitat = int(input("Quants paquets de sobres DIN C5 es vendran? "))
                        if (estocSobres['C5'] - quantitat) > 40:
                            estocSobres['C5'] -= quantitat
                            productesComprar += 1
                            if quantitat >= 4:
                                {zonaClient}[client] += 22.95 * quantitat * 0.96
                                aPagar.append(22.95 * quantitat * 0.96)
                            else:
                                {zonaClient}[client] += 22.95 * quantitat
                                aPagar.append(22.95 * quantitat)
                            print(f"Compra de {quantitat} paquets de sobres DIN C5 realitzada correctament.")
                            print(" ")
                        else:
                            print("No hi ha prou estoc per realitzar aquesta compra.")
                            print(" ")
                    elif opcio == 3:
                        quantitat = int(input("Quants paquets de sobres DIN C4 es vendran? "))
                        if (estocSobres['C4'] - quantitat) > 60:
                            estocSobres['C4'] -= quantitat
                            productesComprar += 1
                            if quantitat >= 4:
                                {zonaClient}[client] += 26.74 * quantitat * 0.95
                                aPagar.append(26.74 * quantitat * 0.95)
                            else:
                                {zonaClient}[client] += 26.74 * quantitat
                                aPagar.append(26.74 * quantitat)
                            print(f"Compra de {quantitat} paquets de sobres DIN C4 realitzada correctament.")
                            print(" ")
                        else:
                            print("No hi ha prou estoc per realitzar aquesta compra.")
                            print(" ")
                    elif opcio == 4:
                        quantitat = int(input("Quants paquets de sobres DIN C3 es vendran? "))
                        if (estocSobres['C3'] - quantitat) > 30:
                            estocSobres['C3'] -= quantitat
                            productesComprar += 1
                            if quantitat >= 4:
                                {zonaClient}[client] += 32.68 * quantitat * 0.94
                                aPagar.append(32.68 * quantitat * 0.94)
                            else:
                                {zonaClient}[client] += 32.68 * quantitat
                                aPagar.append(32.68 * quantitat)
                            print(f"Compra de {quantitat} paquets de sobres DIN C3 realitzada correctament.")
                            print(" ")
                        else:
                            print("No hi ha prou estoc per realitzar aquesta compra.")
                            print(" ")
                    elif opcio == 5:
                        quantitat = int(input("Quants paquets de sobres DIN C2 es vendran? "))
                        if (estocSobres['C2'] - quantitat) > 20:
                            estocSobres['C2'] -= quantitat
                            productesComprar += 1
                            if quantitat >= 4:
                                {zonaClient}[client] += 35.45 * quantitat * 0.93
                                aPagar.append(35.45 * quantitat * 0.93)
                            else:
                                {zonaClient}[client] += 35.45 * quantitat
                                aPagar.append(35.45 * quantitat)
                            print(f"Compra de {quantitat} paquets de sobres DIN C2 realitzada correctament.")
                            print(" ")
                        else:
                            print("No hi ha prou estoc per realitzar aquesta compra.")
                            print(" ")
                    else:
                        print("Opció incorrecta. Si us plau, introdueix una opció vàlida.")
                        print(" ")
            elif funcioVendes == 7:
                print("Mostrant quantitat d'€ invertits en paper/sobres per client: ")
                print("Zona A: ")
                for client in clientsZonaA:
                    print(f"- {client}: {round(clientsZonaA[client], 2)}€")
                print(" ")
                print("Zona B: ")
                for client in clientsZonaB:
                    print(f"- {client}: {round(clientsZonaB[client], 2)}€")
                print(" ")
                print("Zona C: ")
                for client in clientsZonaC:
                    print(f"- {client}: {round(clientsZonaC[client], 2)}€")
                print(" ")
            elif funcioVendes == 8:
                print("Gràcies per utilitzar el programa. Tancant la sessió...")
                time.sleep(1)
                break