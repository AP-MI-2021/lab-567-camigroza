from Logic.CRUD import adauga_cheltuiala
from Tests.test_all import run_all_tests
from UI.console import run_menu


def main():
    run_all_tests()
    lista = []
    lista = adauga_cheltuiala(1, 1000, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(1, 500, "25.10.2021", "alte cheltuieli", lista)
    lista = adauga_cheltuiala(2, 750, "24.10.2021", "canal", lista)
    run_menu(lista)


if __name__ == '__main__':
  main()