from Domain.cheltuiala import get_nr_ap
from Logic.CRUD import sterge_cheltuiala


def stergere_cheltuieli(nr_ap, lista):
    '''
    Sterge toate cheltuielile pentru un apartament dat
    :param nr_ap: int
    :param lista: o lista de cheltuieli
    :return: lista de cheltuieli obtinuta prin stergerea tuturor cheltuielilor pentru apartamentul dat
    '''
    for cheltuiala in lista:
        if get_nr_ap(cheltuiala) == nr_ap:
            lista = sterge_cheltuiala(nr_ap, lista)
    return lista