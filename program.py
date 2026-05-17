import datetime

preces = []

def pievienot_preces():
    nosaukums = input("Preces nosaukums: ")
    materials = input("Materials: ")
    daudzums = int(input("Daudzums:"))
    cena = float(input("Cena:"))
    garantija_gados = int(input("Garantijas termiņš (gados): "))

    garantijas_beigas = datetime.date.today().replace(year=datetime.date.today().year + garantija_gados)

    prece = {
        "nosaukums": nosaukums,
        "materials": materials,
        "daudzums": daudzums,
        "cena": cena,
        "garantijas_beigas": garantijas_beigas
    }

    preces.append(prece)
    print("Prece pievienota!")

def paradit_preces():
    if not preces:
        print("Nav nevienas preces.")
        return

    for p in preces:
        print(f"{p['nosaukums']}, {p['materials']}, Daudzums: {p['daudzums']}, Cena: {p['cena']}, Garantija līdz: {p['garantijas_beigas']}")
    print()

def atrast_preces():
    mekle = input("Iavadi preces nosaukumu: ")
    for p in preces:
        if p["nosaukums"].lower() == mekle.lower():
            print("Atrastā prece:")
            print(p)
            return
        print("Prece nav atrasta.")

def parbaudit_garantijas():
    sodiena = datetime.date.today()
    for p in preces:
        if (p["garantijas_beigas"]- sodiena).days <= 30:
            print(f"Precei '{p['nosaukums']}' drīz beigsies garantija!")
    print()

while True:
    print("1 - Pievienot preci")
    print("2 - Parādīt visas preces ")
    print("3 - Atrast preci")
    print("4 - Pārbaudīt garantijas")
    print("0 - Iziet")

    izvelne = input("Izvēlies darbību:")

    if izvelne == "1":
        pievienot_preces()
    elif izvelne == "2":
        paradit_preces()
    elif izvelne == "3":
        atrast_preces()
    elif izvelne == "4":
        parbaudit_garantijas()
    elif izvelne == "0":
        break
    else:
        print("Nepareiza izvēle.")
