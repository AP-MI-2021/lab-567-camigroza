from Domain.cheltuiala import creeaza_cheltuiala, get_nr_ap


def adauga_cheltuiala(nr_ap, suma, data, tip, lista):
    '''
    Adauga cheltuiala intr-o lista
    :param nr_ap: int
    :param suma: float
    :param data: string
    :param tip: string
    :param lista: o lista de cheltuieli
    :return: o lista care contine atat elementele vechi, cat si elementele noi
    '''
    cheltuiala = creeaza_cheltuiala(nr_ap, suma, data, tip)
    return lista + [cheltuiala]


def get_by_nr_ap(nr_ap, lista):
    '''
    Indica cheltuiala cu numarul apartamentului dat dintr-o lista
    :param nr_ap: int
    :param lista: o lista de cheltuieli
    :return: cheltuiala cu numarul apartamentului dat din lista sau None, daca aceasta nu exista
    '''
    for cheltuiala in lista:
        if get_nr_ap(cheltuiala) == nr_ap:
            return cheltuiala
    return None


def sterge_cheltuiala(nr_ap, lista):
    '''
    Sterge o cheltuiala cu numarul apartamentului dat din lista
    :param nr_ap: int
    :param lista: o lista de cheltuieli
    :return: o lista de cheltuieli, fara elementul cu numarul apartamentului dat
    '''
    return [cheltuiala for cheltuiala in lista if get_nr_ap(cheltuiala) != nr_ap]


def modifica_cheltuiala(nr_ap, suma, data, tip, lista):
    '''
    Modifica o cheltuiala cu numarul apartamentului dat
    :param nr_ap: int
    :param suma: float
    :param data: string
    :param tip: string
    :param lista: o lista de cheltuieli
    :return: lista modificata
    '''
    lista_noua = []
    for cheltuiala in lista:
        if get_nr_ap(cheltuiala) == nr_ap:
            cheltuiala_noua = creeaza_cheltuiala(nr_ap, suma, data, tip)
            lista_noua.append(cheltuiala_noua)
        else:
            lista_noua.append(cheltuiala)
    return lista_noua