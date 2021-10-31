from Domain.cheltuiala import creeaza_cheltuiala, get_nr_ap, get_id, get_data


def adauga_cheltuiala(id, nr_ap, suma, data, tip, lista):
    '''
    Adauga cheltuiala intr-o lista
    :param id: int
    :param nr_ap: int
    :param suma: float
    :param data: string
    :param tip: string
    :param lista: o lista de cheltuieli
    :return: o lista care contine atat elementele vechi, cat si elementele noi
    '''
    if get_by_id(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    cheltuiala = creeaza_cheltuiala(id, nr_ap, suma, data, tip)
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


def get_by_id(id, lista):
    '''
    Indica cheltuiala cu id-ul dat dintr-o lista
    :param id: int
    :param lista: o lista de cheltuieli
    :return: cheltuiala cu id-ul dat din lista sau None, daca aceasta nu exista
    '''
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            return cheltuiala
    return None


def get_by_data(data, lista):
    '''
    Indica cheltuiala cu data data dintr-o lista
    :param data: string
    :param lista: o lista de cheltuieli
    :return: cheltuiala cu data data din lista sau None, daca aceasta nu exista
    '''
    for cheltuiala in lista:
        if get_data(cheltuiala) == data:
            return cheltuiala
    return None


def sterge_cheltuiala(nr_ap, lista):
    '''
    Sterge o cheltuiala cu numarul apartamentului dat din lista
    :param nr_ap: int
    :param lista: o lista de cheltuieli
    :return: o lista de cheltuieli, fara elementul cu numarul apartamentului dat
    '''
    if get_by_nr_ap(nr_ap, lista) is None:
        raise ValueError("Nu exista o cheltuiala cu numarul apartamentului dat!")
    return [cheltuiala for cheltuiala in lista if get_nr_ap(cheltuiala) != nr_ap]


def modifica_cheltuiala(id, nr_ap, suma, data, tip, lista):
    '''
    Modifica o cheltuiala cu numarul apartamentului dat
    :param id: int
    :param nr_ap: int
    :param suma: float
    :param data: string
    :param tip: string
    :param lista: o lista de cheltuieli
    :return: lista modificata
    '''
    if get_by_nr_ap(nr_ap, lista) is None:
        raise ValueError("Nu exista o cheltuiala cu numarul apartamentului dat!")
    lista_noua = []
    for cheltuiala in lista:
        if get_nr_ap(cheltuiala) == nr_ap:
            cheltuiala_noua = creeaza_cheltuiala(id, nr_ap, suma, data, tip)
            lista_noua.append(cheltuiala_noua)
        else:
            lista_noua.append(cheltuiala)
    return lista_noua