from Domain.cheltuiala import get_nr_ap, get_suma, get_data, get_tip, get_id
from Logic.CRUD import adauga_cheltuiala, get_by_nr_ap, sterge_cheltuiala, modifica_cheltuiala, get_by_id


def test_adauga_cheltuiala():
    lista = []
    lista = adauga_cheltuiala(1, 1, 1000, "23.10.2021", "intretinere", lista)

    assert len(lista) == 1
    assert get_id(get_by_nr_ap(1, lista)) == 1
    assert get_nr_ap(get_by_nr_ap(1, lista)) == 1
    assert get_suma(get_by_nr_ap(1, lista)) == 1000
    assert get_data(get_by_nr_ap(1, lista)) == "23.10.2021"
    assert get_tip(get_by_nr_ap(1, lista)) == "intretinere"


def test_sterge_cheltuiala():
    lista = []
    lista = adauga_cheltuiala(1, 1, 1000, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(2, 2, 750, "24.10.2021", "canal", lista)

    lista = sterge_cheltuiala(1, lista)
    assert len(lista) == 1
    assert get_by_id(1, lista) is None
    assert get_by_id(2, lista) is not None

    try:
        lista = sterge_cheltuiala(3, lista)
        assert False
    except ValueError:
        assert len(lista) == 1
        assert get_by_id(2, lista) is not None
    except Exception:
        assert False


def test_modifica_cheltuiala():
    lista = []
    lista = adauga_cheltuiala(1, 1, 1000, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(2, 2, 750, "24.10.2021", "canal", lista)

    lista = modifica_cheltuiala(2, 2, 1000, "23.10.2021", "intretinere", lista)
    assert len(lista) == 2
    assert get_id(get_by_nr_ap(1, lista)) == 1
    assert get_nr_ap(get_by_nr_ap(1, lista)) == 1
    assert get_suma(get_by_nr_ap(1, lista)) == 1000
    assert get_data(get_by_nr_ap(1, lista)) == "23.10.2021"
    assert get_tip(get_by_nr_ap(1, lista)) == "intretinere"
    assert get_id(get_by_nr_ap(2, lista)) == 2
    assert get_nr_ap(get_by_nr_ap(2, lista)) == 2
    assert get_suma(get_by_nr_ap(2, lista)) == 1000
    assert get_data(get_by_nr_ap(2, lista)) == "23.10.2021"
    assert get_tip(get_by_nr_ap(2, lista)) == "intretinere"
