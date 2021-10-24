from Logic.CRUD import adauga_cheltuiala
from Logic.functionalitati import stergere_cheltuieli


def test_stergere_cheltuieli():
    lista = []
    lista = adauga_cheltuiala(1, 1000, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(1, 500, "25.10.2021", "alte cheltuieli", lista)
    lista = adauga_cheltuiala(2, 750, "24.10.2021", "canal", lista)

    lista = stergere_cheltuieli(1, lista)

    assert len(lista) == 1
