from Domain.cheltuiala import get_suma, get_id
from Logic.CRUD import adauga_cheltuiala, get_by_nr_ap
from Logic.functionalitati import stergere_cheltuieli, aduna_valoare, max_cheltuiala_per_tip, \
    ordonare_descrescator_suma, sume_lunare_per_apartament


def test_stergere_cheltuieli():
    lista = []
    lista = adauga_cheltuiala(1, 1, 1000, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(2, 1, 500, "25.10.2021", "alte cheltuieli", lista)
    lista = adauga_cheltuiala(3, 2, 750, "24.10.2021", "canal", lista)

    lista = stergere_cheltuieli(2, lista)

    assert len(lista) == 2


def test_aduna_valoare():
    lista = []
    lista = adauga_cheltuiala(1, 1, 1000, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(2, 2, 500, "25.10.2021", "alte cheltuieli", lista)
    lista = adauga_cheltuiala(3, 3, 750, "23.10.2021", "canal", lista)

    lista = aduna_valoare(100, "23.10.2021", lista)

    assert get_suma(get_by_nr_ap(1, lista)) == 1100
    assert get_suma(get_by_nr_ap(3, lista)) == 850


def test_max_cheltuiala_per_tip():
    lista = []
    lista = adauga_cheltuiala(1, 1, 1000, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(2, 2, 500, "25.10.2021", "alte cheltuieli", lista)
    lista = adauga_cheltuiala(3, 3, 750, "23.10.2021", "canal", lista)
    lista = adauga_cheltuiala(4, 3, 950, "23.10.2021", "canal", lista)

    rezultat = max_cheltuiala_per_tip(lista)

    assert len(rezultat) == 3
    assert rezultat["intretinere"] == 1000
    assert rezultat["alte cheltuieli"] == 500
    assert rezultat["canal"] == 950


def test_ordonare_descrescator_suma():
    lista = []
    lista = adauga_cheltuiala(1, 1, 1000, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(2, 2, 500, "25.10.2021", "alte cheltuieli", lista)
    lista = adauga_cheltuiala(3, 3, 750, "23.10.2021", "canal", lista)
    lista = adauga_cheltuiala(4, 3, 950, "23.10.2021", "canal", lista)

    rezultat = ordonare_descrescator_suma(lista)

    assert get_id(rezultat[0]) == 1
    assert get_id(rezultat[1]) == 4
    assert get_id(rezultat[2]) == 3
    assert get_id(rezultat[3]) == 2


def test_sume_lunare_per_apartament():
    lista = []
    lista = adauga_cheltuiala(1, 1, 1000, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(2, 2, 500, "25.11.2021", "alte cheltuieli", lista)
    lista = adauga_cheltuiala(3, 3, 750, "23.04.2021", "canal", lista)
    lista = adauga_cheltuiala(4, 3, 950, "23.04.2021", "canal", lista)

    rezultat = sume_lunare_per_apartament(lista)

    assert len(rezultat) == 3
    assert rezultat[1] == {'luna': '10', 'suma': 1000}
    assert rezultat[2] == {'luna': '11', 'suma': 500}
    assert rezultat[3] == {'luna': '04', 'suma': 1700}
