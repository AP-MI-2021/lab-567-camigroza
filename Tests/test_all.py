from Tests.test_CRUD import test_adauga_cheltuiala, test_sterge_cheltuiala, test_modifica_cheltuiala
from Tests.test_domain import test_cheltuiala
from Tests.test_functionalitati import test_stergere_cheltuieli


def run_all_tests():
    test_cheltuiala()
    test_adauga_cheltuiala()
    test_sterge_cheltuiala()
    test_modifica_cheltuiala()
    test_stergere_cheltuieli()