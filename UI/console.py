from Domain.cheltuiala import to_string
from Logic.CRUD import adauga_cheltuiala, sterge_cheltuiala, modifica_cheltuiala
from Logic.functionalitati import stergere_cheltuieli, aduna_valoare, max_cheltuiala_per_tip, \
    ordonare_descrescator_suma, sume_lunare_per_apartament


def print_menu():
    print("1. Adaugare cheltuiala")
    print("2. Stergere cheltuiala")
    print("3. Modificare cheltuiala")
    print("4. Stergerea tuturor cheltuielilor pentru un apartament dat")
    print("5. Adunarea unei valori la toate cheltuielile dintr-o data citita")
    print("6. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuiala")
    print("7. Ordonarea cheltuielilor descrescator dupa suma")
    print("8. Afisarea sumelor lunare pentru fiecare apartament")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare cheltuiala")
    print("x. Iesire")


def ui_adauga_cheltuiala(lista, undo_list, redo_list, valori):
    try:
        if len(valori) == 0:
            id = int(input("Dati id-ul: "))
            nr_ap = int(input("Dati numarul apartamentului: "))
            suma = float(input("Dati suma: "))
            data = input("Dati data, sub forma DD.MM.YYYY: ")
            tip = input("Dati unul dintre tipurile 'intretinere', 'canal', 'alte cheltuieli': ")
        else:
            id = valori[0]
            nr_ap = valori[1]
            suma = valori[2]
            data = valori[3]
            tip = valori[4]
        rezultat = adauga_cheltuiala(id, nr_ap, suma, data, tip, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_sterge_cheltuiala(lista, undo_list, redo_list, valori):
    try:
        if len(valori) == 0:
            id = int(input("Dati id-ul cheltuielii de sters: "))
        else:
            id = valori[0]
        rezultat = sterge_cheltuiala(id, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_modifica_cheltuiala(lista, undo_list, redo_list, valori):
    try:
        if len(valori) == 0:
            id = int(input("Dati id-ul: "))
            nr_ap = int(input("Dati numarul apartamentului cheltuielii de modificat: "))
            suma = float(input("Dati noua suma: "))
            data = input("Dati noua data: ")
            tip = input("Dati noul tip: ")
        else:
            id = valori[0]
            nr_ap = valori[1]
            suma = valori[2]
            data = valori[3]
            tip = valori[4]
        rezultat = modifica_cheltuiala(id, nr_ap, suma, data, tip, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def show_all(lista):
    for cheltuiala in lista:
        print(to_string(cheltuiala))


def ui_stergere_cheltuieli(lista, undo_list, redo_list, valori):
    try:
        if len(valori) == 0:
            nr_ap = int(input("Dati numarul apartamentului pentru care trebuie sterse toate cheltuielile: "))
        else:
            nr_ap = valori[0]
        rezultat = stergere_cheltuieli(nr_ap, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_aduna_valoare(lista, undo_list, redo_list, valori):
    try:
        if len(valori) == 0:
            data = input("Dati data: ")
            valoare = float(input("Dati valoarea pe care doriti sa o adunati la toate cheltuielile din data citita: "))
        else:
            data = valori[0]
            valoare = valori[1]
        rezultat = aduna_valoare(valoare, data, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_max_cheltuiala_per_tip(lista):
    rezultat = {}
    rezultat = max_cheltuiala_per_tip(lista)
    for tip in rezultat:
        print("Tipul '{}' are cheltuiala maxima in valoare de {} ron".format(tip, rezultat[tip]))


def ui_ordonare_descrescator_suma(lista, undo_list, redo_list):
    rezultat = ordonare_descrescator_suma(lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat


def ui_sume_lunare_per_apartament(lista):
    rezultat = sume_lunare_per_apartament(lista)
    dict_luni = {
        "01": "Ianuarie",
        "02": "Februarie",
        "03": "Martie",
        "04": "Aprilie",
        "05": "Mai",
        "06": "Iunie",
        "07": "Iulie",
        "08": "August",
        "09": "Septembrie",
        "10": "Octombrie",
        "11": "Noiembrie",
        "12": "Decembrie"
    }
    for nr_ap in rezultat:
        print("Apartamentul cu numarul {} are pana in luna {} o cheltuiala in valoare de {} ron".format(
            nr_ap,
            dict_luni[rezultat[nr_ap]['luna']],
            rezultat[nr_ap]['suma']
    ))


def undo(lista, undo_list, redo_list):
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
    else:
        print("Nu se poate face undo!")
    return lista


def redo(lista, undo_list, redo_list):
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    else:
        print("Nu se poate face redo!")
    return lista


def run_menu(lista):
    undo_list = []
    redo_list = []
    valori = []
    while True:
        print_menu()
        optiune = (input("Dati optiunea: "))
        if optiune == "1":
            lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)
        elif optiune == "2":
            lista = ui_sterge_cheltuiala(lista, undo_list, redo_list, valori)
        elif optiune == "3":
            lista = ui_modifica_cheltuiala(lista, undo_list, redo_list, valori)
        elif optiune == "4":
            lista = ui_stergere_cheltuieli(lista, undo_list, redo_list, valori)
        elif optiune == "5":
            lista = ui_aduna_valoare(lista, undo_list, redo_list, valori)
        elif optiune == "6":
            ui_max_cheltuiala_per_tip(lista)
        elif optiune == "7":
            lista = ui_ordonare_descrescator_suma(lista, undo_list, redo_list)
        elif optiune == "8":
            ui_sume_lunare_per_apartament(lista)
        elif optiune == "u":
            lista = undo(lista, undo_list, redo_list)
            #if len(undo_list) > 0:
                #redo_list.append(lista)
                #lista = undo_list.pop()
            #else:
                #print("Nu se poate face undo!")
        elif optiune == "r":
            lista = redo(lista, undo_list, redo_list)
            #if len(redo_list) > 0:
                #undo_list.append(lista)
                #lista = redo_list.pop()
            #else:
                #print("Nu se poate face redo!")
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati:")