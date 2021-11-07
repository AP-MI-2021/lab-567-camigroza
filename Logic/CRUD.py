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
    if nr_ap < 0:
        raise ValueError("Numarul apartamentului nu poate fi negativ!")
    if tip != "intretinere" and tip != "canal" and tip != "alte cheltuieli":
        raise ValueError("Dati un tip din cele precizate!")
    if len(data) < 10 or (data[2] != '.' and data[5] != '.'):
        raise ValueError("Structura datei nu este conform cerintei!")
    ziua = data[0] + data[1]
    luna = data[3] + data[4]
    if int(ziua) > 31:
        raise ValueError("O luna nu poate avea mai mult de 31 zile!")
    if int(luna) > 12:
        raise ValueError("Nu exista mai mult de 12 luni in an!")
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


def sterge_cheltuiala(id, lista):
    '''
    Sterge o cheltuiala cu id-ul dat din lista
    :param id: int
    :param lista: o lista de cheltuieli
    :return: o lista de cheltuieli, fara elementul cu id-ul dat
    '''
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista o cheltuiala cu id-ul dat!")
    return [cheltuiala for cheltuiala in lista if get_id(cheltuiala) != id]


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
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista o cheltuiala cu id-ul dat!")
    lista_noua = []
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            cheltuiala_noua = creeaza_cheltuiala(id, nr_ap, suma, data, tip)
            lista_noua.append(cheltuiala_noua)
        else:
            lista_noua.append(cheltuiala)
    return lista_noua
