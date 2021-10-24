def creeaza_cheltuiala(nr_ap, suma, data, tip):
    '''
    Creeza un dictionar ce reprezinta o cheltuiala
    :param nr_ap: int
    :param suma: float
    :param data: string
    :param tip: string
    :return: un dictionar ce reprezinta o cheltuiala
    '''
    return {
        "nr_ap": nr_ap,
        "suma": suma,
        "data": data,
        "tip": tip
    }


def get_nr_ap(cheltuiala):
    '''
    Indica numarul apartamentului unei cheltuieli
    :param cheltuiala: dictionar ce contine o cheltuiala
    :return: numarul apartamentului cheltuielii
    '''
    return cheltuiala["nr_ap"]


def get_suma(cheltuiala):
    '''
    Indica suma unei cheltuieli
    :param cheltuiala: un dictionar ce contine o cheltuiala
    :return: suma cheltuielii
    '''
    return cheltuiala["suma"]


def get_data(cheltuiala):
    '''
    Indica data unei cheltuieli
    :param cheltuiala: un dictionar ce contine o cheltuiala
    :return: data cheltuielii
    '''
    return cheltuiala["data"]


def get_tip(cheltuiala):
    '''
    Indica tipul unei cheltuieli
    :param cheltuiala: un dictionar ce contine o cheltuiala
    :return: tipul cheltuielii
    '''
    return cheltuiala["tip"]


def to_string(cheltuiala):
    return "Numar apartament: {}, Suma: {}, Data: {}, Tip: {}".format(
        get_nr_ap(cheltuiala),
        get_suma(cheltuiala),
        get_data(cheltuiala),
        get_tip(cheltuiala)
    )