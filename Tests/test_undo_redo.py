from Domain.cheltuiala import get_nr_ap, get_suma, get_data, get_tip, get_id
from Logic.CRUD import get_by_id
from UI.console import ui_adauga_cheltuiala, undo, redo, ui_sterge_cheltuiala, ui_modifica_cheltuiala, \
    ui_stergere_cheltuieli, ui_aduna_valoare, ui_ordonare_descrescator_suma


def test_undo_redo():
#1# lista initiala goala
    lista = []

    undo_list = []
    redo_list = []

#2# adaugam o cheltuiala
    valori = [1, 1, 100, "07.11.2021", "intretinere"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)
#3# adaugam inca o cheltuiala
    valori = [2, 2, 200, "08.11.2021", "canal"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)
#4# adaugam inca o cheltuiala
    valori = [3, 3, 300, "09.11.2021", "alte cheltuieli"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)

    assert len(lista) == 3

#5# undo scoate ultima cheltuiala adaugata
    lista = undo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is not None
    assert get_by_id(3, lista) is None

#6# inca un undo scoate penultima cheltuiala adaugata
    lista = undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is None
    assert get_by_id(3, lista) is None

#7# inca un undo scoate si prima cheltuiala adaugata
    lista = undo(lista, undo_list, redo_list)
    assert len(lista) == 0
    assert get_by_id(1, lista) is None
    assert get_by_id(2, lista) is None
    assert get_by_id(3, lista) is None

#8# inca un undo nu face nimic
    lista = undo(lista, undo_list, redo_list)
    assert len(lista) == 0
    assert get_by_id(1, lista) is None
    assert get_by_id(2, lista) is None
    assert get_by_id(3, lista) is None

#9# adaugam trei cheltuieli
    valori = [1, 1, 100, "10.11.2021", "intretinere"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)
    valori = [2, 2, 200, "11.11.2021", "canal"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)
    valori = [3, 3, 300, "12.11.2021", "alte cheltuieli"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)

    assert len(lista) == 3

#10# redo nu face nimic
    lista = redo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is not None
    assert get_by_id(3, lista) is not None

#11# doua undo-uri scot ultimele doua cheltuieli
    lista = undo(lista, undo_list, redo_list)
    lista = undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is None
    assert get_by_id(3, lista) is None

#12# redo anuleaza ultimul undo, daca ultima operatie e undo
    lista =redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is not None
    assert get_by_id(3, lista) is None

#13# redo anuleaza si primul undo
    lista = redo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is not None
    assert get_by_id(3, lista) is not None

#14# doua undo-uri scot ultimele doua cheltuieli
    lista = undo(lista, undo_list, redo_list)
    lista = undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is None
    assert get_by_id(3, lista) is None

#15# adaugam o cheltuiala
    valori = [4, 4, 400, "13.11.2021", "intretinere"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)

    assert len(lista) == 2

#16# redo nu face nimic deoarece ultima operatie nu este undo
    lista = redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id(1, lista) is not None
    assert get_by_id(4, lista) is not None

#17# undo anuleaza adaugarea cheltuielii cu id-ul 4
    lista = undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert get_by_id(1, lista) is not None
    assert get_by_id(4, lista) is None

#18# undo anuleaza adaugarea cheltuielii cu id-ul 1
#practic se continua sirul de undo de la punctul 14
    lista = undo(lista, undo_list, redo_list)
    assert len(lista) == 0
    assert get_by_id(1, lista) is None
    assert get_by_id(4, lista) is None

#19# se anuleaza ultimele doua undo-uri
    lista = redo(lista, undo_list, redo_list)
    lista = redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is None
    assert get_by_id(3, lista) is None
    assert get_by_id(4, lista) is not None

#20# redo nu face nimic
    lista = redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is None
    assert get_by_id(3, lista) is None
    assert get_by_id(4, lista) is not None

#test undo/redo la stergere cheltuiala
    lista = []
    valori = [1, 1, 100, "10.11.2021", "intretinere"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)
    valori = [2, 2, 200, "11.11.2021", "canal"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)
    valori = [3, 3, 300, "12.11.2021", "alte cheltuieli"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)
    valori = [1]
    lista = ui_sterge_cheltuiala(lista, undo_list, redo_list, valori)
    assert len(lista) == 2
    assert get_by_id(1, lista) is None
    assert get_by_id(2, lista) is not None
    assert get_by_id(3, lista) is not None
    lista = undo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is not None
    assert get_by_id(3, lista) is not None
    lista = redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id(1, lista) is None
    assert get_by_id(2, lista) is not None
    assert get_by_id(3, lista) is not None

#test undo/redo la modifica cheltuiala
    lista = []
    valori = [1, 1, 100, "10.11.2021", "intretinere"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)
    valori = [2, 2, 200, "11.11.2021", "canal"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)
    valori = [3, 3, 300, "12.11.2021", "alte cheltuieli"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)
    valori = [1, 10, 1000, "12.12.2021", "alte cheltuieli"]
    lista = ui_modifica_cheltuiala(lista, undo_list, redo_list, valori)
    assert len(lista) == 3
    assert get_nr_ap(get_by_id(1, lista)) == 10
    assert get_suma(get_by_id(1, lista)) == 1000
    assert get_data(get_by_id(1, lista)) == "12.12.2021"
    assert get_tip(get_by_id(1, lista)) == "alte cheltuieli"
    lista = undo(lista, undo_list, redo_list)
    assert get_nr_ap(get_by_id(1, lista)) == 1
    assert get_suma(get_by_id(1, lista)) == 100
    assert get_data(get_by_id(1, lista)) == "10.11.2021"
    assert get_tip(get_by_id(1, lista)) == "intretinere"
    lista = redo(lista, undo_list, redo_list)
    assert get_nr_ap(get_by_id(1, lista)) == 10
    assert get_suma(get_by_id(1, lista)) == 1000
    assert get_data(get_by_id(1, lista)) == "12.12.2021"
    assert get_tip(get_by_id(1, lista)) == "alte cheltuieli"

#test undo/redo la stergere cheltuieli
    lista = []
    valori = [1, 1, 100, "10.11.2021", "intretinere"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)
    valori = [2, 1, 200, "11.11.2021", "canal"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)
    valori = [3, 3, 300, "12.11.2021", "alte cheltuieli"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)
    valori = [1]
    lista = ui_stergere_cheltuieli(lista, undo_list, redo_list, valori)
    assert len(lista) == 1
    assert get_by_id(1, lista) is None
    assert get_by_id(2, lista) is None
    assert get_by_id(3, lista) is not None
    lista = undo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is not None
    assert get_by_id(3, lista) is not None
    lista = redo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert get_by_id(1, lista) is None
    assert get_by_id(2, lista) is None
    assert get_by_id(3, lista) is not None

#test undo/redo la aduna valoare
    lista = []
    valori = [1, 1, 100, "10.11.2021", "intretinere"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)
    valori = [2, 1, 200, "11.11.2021", "canal"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)
    valori = [3, 3, 300, "11.11.2021", "alte cheltuieli"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)
    valori = ["11.11.2021", 100]
    lista = ui_aduna_valoare(lista, undo_list, redo_list, valori)
    assert get_suma(get_by_id(1, lista)) == 100
    assert get_suma(get_by_id(2, lista)) == 300
    assert get_suma(get_by_id(3, lista)) == 400
    lista = undo(lista, undo_list, redo_list)
    assert get_suma(get_by_id(1, lista)) == 100
    assert get_suma(get_by_id(2, lista)) == 200
    assert get_suma(get_by_id(3, lista)) == 300
    lista = redo(lista, undo_list, redo_list)
    assert get_suma(get_by_id(1, lista)) == 100
    assert get_suma(get_by_id(2, lista)) == 300
    assert get_suma(get_by_id(3, lista)) == 400

#test undo/redo la ordonare descrescator dupa suma
    lista = []
    valori = [1, 1, 100, "10.11.2021", "intretinere"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)
    valori = [2, 1, 200, "11.11.2021", "canal"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)
    valori = [3, 3, 300, "11.11.2021", "alte cheltuieli"]
    lista = ui_adauga_cheltuiala(lista, undo_list, redo_list, valori)
    lista = ui_ordonare_descrescator_suma(lista, undo_list, redo_list)
    assert get_id(lista[0]) == 3
    assert get_id(lista[1]) == 2
    assert get_id(lista[2]) == 1
    lista = undo(lista, undo_list, redo_list)
    assert get_id(lista[0]) == 1
    assert get_id(lista[1]) == 2
    assert get_id(lista[2]) == 3
    lista = redo(lista, undo_list, redo_list)
    assert get_id(lista[0]) == 3
    assert get_id(lista[1]) == 2
    assert get_id(lista[2]) == 1
