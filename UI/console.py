from Domain.cheltuiala import to_string
from Logic.CRUD import adauga_cheltuiala, sterge_cheltuiala, modifica_cheltuiala
from Logic.functionalitati import stergere_cheltuieli


def print_menu():
    print("1. Adaugare cheltuiala")
    print("2. Stergere cheltuiala")
    print("3. Modificare cheltuiala")
    print("4. Stergerea tuturor cheltuielilor pentru un apartament dat")
    print("a. Afisare cheltuiala")
    print("x. Iesire")


def ui_adauga_cheltuiala(lista):
    nr_ap = int(input("Dati numarul apartamentului: "))
    suma = float(input("Dati suma: "))
    data = input("Dati data, sub forma DD.MM.YYYY: ")
    tip = input("Dati unul dintre tipurile 'intretinere', 'canal', 'alte cheltuieli': ")
    return adauga_cheltuiala(nr_ap, suma, data, tip, lista)


def ui_sterge_cheltuiala(lista):
    nr_ap = int(input("Dati numarul apartamentului cheltuielii de sters: "))
    return sterge_cheltuiala(nr_ap, lista)


def ui_modifica_cheltuiala(lista):
    nr_ap = int(input("Dati numarul apartamentului cheltuielii de modificat: "))
    suma = float(input("Dati noua suma: "))
    data = input("Dati noua data: ")
    tip = input("Dati noul tip: ")
    return modifica_cheltuiala(nr_ap, suma, data, tip, lista)


def show_all(lista):
    for cheltuiala in lista:
        print(to_string(cheltuiala))


def ui_stergere_cheltuieli(lista):
    nr_ap = int(input("Dati numarul apartamentului pentru care trebuie sterse toate cheltuielile: "))
    return stergere_cheltuieli(nr_ap, lista)


def run_menu(lista):
    while True:
        print_menu()
        optiune = (input("Dati optiunea: "))
        if optiune == "1":
            lista = ui_adauga_cheltuiala(lista)
        elif optiune == "2":
            lista = ui_sterge_cheltuiala(lista)
        elif optiune == "3":
            lista = ui_modifica_cheltuiala(lista)
        elif optiune == "4":
            lista = ui_stergere_cheltuieli(lista)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati:")