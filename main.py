import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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

proveidors = {"PaperVIP": 0, "ExpressPapereria": 0, "Paper&Co": 0}
compradorsZona1 = ["Naturgraf", "ReciclatPrint", "Fustaprint"]
compradorsZona2 = ["TecnoGràfic", "EcoArts", "FustaStamp"]
compradorsZona3 = ["coScript", "SostenPack", "CelluArts"]

while True:
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
        2) Consultar preu de paper i sobres
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
                                capital -= (6.45 * quantitat) * 0.97
                                proveidors[proveidorPaper] += (6.45 * quantitat) * 0.97
                            else:
                                capital -= 6.45 * quantitat
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
                                capital -= (7.13 * quantitat) * 0.96
                                proveidors[proveidorPaper] += (7.13 * quantitat) * 0.96
                            else:
                                capital -= 7.13 * quantitat
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
                                capital -= (7.98 * quantitat) * 0.95
                                proveidors[proveidorPaper] += (6.45 * quantitat) * 0.95
                            else:
                                capital -= 7.98 * quantitat
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
                                capital -= (37.65 * quantitat) * 0.98
                                proveidors[proveidorPaper] += (37.65 * quantitat) * 0.98
                            else:
                                capital -= 37.65 * quantitat
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
                                capital -= (11.34 * quantitat) * 0.94
                                proveidors[proveidorPaper] += (11.34 * quantitat) * 0.94
                            else:
                                capital -= 11.34 * quantitat
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
                                capital -= (58.45 * quantitat) * 0.97
                                proveidors[proveidorPaper] += (37.65 * quantitat) * 0.97
                            else:
                                capital -= 58.45 * quantitat
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
                                capital -= (18.95 * quantitat) * 0.93
                                proveidors[proveidorPaper] += (18.95 * quantitat) * 0.93
                            else:
                                capital -= 18.95 * quantitat
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
                                capital -= (33.45 * quantitat) * 0.97
                                proveidors[proveidorSobres] += (33.45 * quantitat) * 0.97
                            else:
                                capital -= 33.45 * quantitat
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
                                capital -= (30.58 * quantitat) * 0.96
                                proveidors[proveidorSobres] += (30.58 * quantitat) * 0.96
                            else:
                                capital -= 30.58 * quantitat
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
                                capital -= (24.78 * quantitat) * 0.95
                                proveidors[proveidorSobres] += (24.78 * quantitat) * 0.95
                            else:
                                capital -= 24.78 * quantitat
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
                                capital -= (20.80 * quantitat) * 0.94
                                proveidors[proveidorSobres] += (20.80 * quantitat) * 0.94
                            else:
                                capital -= 20.80 * quantitat
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
                                capital -= (16.15 * quantitat) * 0.93
                                proveidors[proveidorSobres] += (16.15 * quantitat) * 0.93
                            else:
                                capital -= 16.15 * quantitat
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
        print("Vendes")