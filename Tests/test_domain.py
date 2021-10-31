from Domain.cheltuiala import creeaza_cheltuiala, get_nr_ap, get_suma, get_data, get_tip, get_id


def test_cheltuiala():
    cheltuiala = creeaza_cheltuiala(1, 1, 1000, "23.10.2021", "intretinere")

    assert get_id(cheltuiala) == 1
    assert get_nr_ap(cheltuiala) == 1
    assert get_suma(cheltuiala) == 1000
    assert get_data(cheltuiala) == "23.10.2021"
    assert get_tip(cheltuiala) == "intretinere"

