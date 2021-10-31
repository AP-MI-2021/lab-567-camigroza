def creeaza_cheltuiala(id, nr_ap, suma, data, tip):
    '''
    Creeza un dictionar ce reprezinta o cheltuiala
    :param id: int
    :param nr_ap: int
    :param suma: float
    :param data: string
    :param tip: string
    :return: un dictionar ce reprezinta o cheltuiala
    '''
    #return {
    #    "nr_ap": nr_ap,
    #    "suma": suma,
    #    "data": data,
    #    "tip": tip
    #}
    return (id, nr_ap, suma, data, tip)


def get_id(cheltuiala):
    '''
    Indica id-ul unei cheltuieli
    :param cheltuiala: dictionar ce contine o cheltuiala
    :return: id-ul cheltuielii
    '''
    #return cheltuiala["id"]
    return cheltuiala[0]


def get_nr_ap(cheltuiala):
    '''
    Indica numarul apartamentului unei cheltuieli
    :param cheltuiala: dictionar ce contine o cheltuiala
    :return: numarul apartamentului cheltuielii
    '''
    #return cheltuiala["nr_ap"]
    return cheltuiala[1]


def get_suma(cheltuiala):
    '''
    Indica suma unei cheltuieli
    :param cheltuiala: un dictionar ce contine o cheltuiala
    :return: suma cheltuielii
    '''
    #return cheltuiala["suma"]
    return cheltuiala[2]


def get_data(cheltuiala):
    '''
    Indica data unei cheltuieli
    :param cheltuiala: un dictionar ce contine o cheltuiala
    :return: data cheltuielii
    '''
    #return cheltuiala["data"]
    return cheltuiala[3]


def get_tip(cheltuiala):
    '''
    Indica tipul unei cheltuieli
    :param cheltuiala: un dictionar ce contine o cheltuiala
    :return: tipul cheltuielii
    '''
    #return cheltuiala["tip"]
    return cheltuiala[4]


def to_string(cheltuiala):
    return "Id: {}, Numar apartament: {}, Suma: {}, Data: {}, Tip: {}".format(
        get_id(cheltuiala),
        get_nr_ap(cheltuiala),
        get_suma(cheltuiala),
        get_data(cheltuiala),
        get_tip(cheltuiala)
    )