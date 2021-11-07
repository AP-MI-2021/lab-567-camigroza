from Logic.CRUD import adauga_cheltuiala
from Tests.test_all import run_all_tests
from UI.command_line_console import menu
from UI.console import run_menu


def main():
    run_all_tests()
    lista = []
    lista = adauga_cheltuiala(1, 1, 1000, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(2, 1, 500, "25.10.2021", "alte cheltuieli", lista)
    lista = adauga_cheltuiala(3, 2, 750, "24.10.2021", "canal", lista)
    lista = adauga_cheltuiala(4, 2, 950, "24.10.2021", "canal", lista)
    '''meniu = input("Daca doriti sa folositi meniul vechi, tastati 'old',"
                  "iar daca doriti sa folositi meniul nou, tastati 'new': ")
    if meniu == 'old':
        run_menu(lista)
    elif meniu == 'new':
        menu(lista)'''
    run_menu(lista)


if __name__ == '__main__':
  main()