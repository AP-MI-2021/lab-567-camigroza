from Domain.cheltuiala import get_nr_ap, get_data, creeaza_cheltuiala, get_id, get_suma, get_tip
from Logic.CRUD import sterge_cheltuiala, get_by_nr_ap, get_by_data


def stergere_cheltuieli(nr_ap, lista):
    '''
    Sterge toate cheltuielile pentru un apartament dat
    :param nr_ap: int
    :param lista: o lista de cheltuieli
    :return: lista de cheltuieli obtinuta prin stergerea tuturor cheltuielilor pentru apartamentul dat
    '''
    if get_by_nr_ap(nr_ap, lista) is None:
        raise ValueError("Nu exista o cheltuiala cu numarul apartamentului dat!")
    for cheltuiala in lista:
        if get_nr_ap(cheltuiala) == nr_ap:
            lista = sterge_cheltuiala(get_id(cheltuiala), lista)
    return lista


def aduna_valoare(valoare, data, lista):
    '''
    Aduna o valoare la toate cheltuielile dintr-o data citita
    :param valoare: float
    :param data: string
    :param lista: o lista de cheltuieli
    :return: lista de cheltuieli in care s-a adunat o valoare la toate cheltuielile din data citita
    '''
    if get_by_data(data, lista) is None:
        raise ValueError("Nu exista o cheltuiala cu data data!")
    lista_noua = []
    for cheltuiala in lista:
        if get_data(cheltuiala) == data:
            cheltuiala_noua = creeaza_cheltuiala(
                get_id(cheltuiala),
                get_nr_ap(cheltuiala),
                get_suma(cheltuiala) + valoare,
                get_data(cheltuiala),
                get_tip(cheltuiala)
            )
            lista_noua.append(cheltuiala_noua)
        else:
            lista_noua.append(cheltuiala)
    return lista_noua


def max_cheltuiala_per_tip(lista):
    '''
    Determina cea mai mare cheltuiala pentru fiecare tip de cheltuiala
    :param lista: o lista de cheltuieli
    :return: un dictionar care are ca si cheie tipul cheltuielii,
            iar ca si valoare, cea mai mare cheltuiala a tipului respectiv
    '''
    rezultat = {}
    for cheltuiala in lista:
        suma = get_suma(cheltuiala)
        tip = get_tip(cheltuiala)
        if tip in rezultat:
            if suma > rezultat[tip]:
                rezultat[tip] = suma
        else:
            rezultat[tip] = suma
    return rezultat


def ordonare_descrescator_suma(lista):
    '''
    Ordoneaza cheltuielile descrescator dupa suma
    :param lista: o lista de cheltuieli
    :return: lista cu cheltuielile ordonate descrescator dupa suma
    '''
    return sorted(lista, key=get_suma, reverse=True)


def sume_lunare_per_apartament(lista):
    '''
    Determina sumele lunare pentru fiecare apartament
    :param lista: o lista de cheltuieli
    :return: un dictionar de tipul 'nested dictionary' care are sintaxa urmatoare:
            {numarul apartamentului, {'luna': luna cheltuielii, 'suma': valoarea sumei respectivei cheltuieli}}
    '''
    rezultat = {}
    for cheltuiala in lista:
        nr_ap = get_nr_ap(cheltuiala)
        suma = get_suma(cheltuiala)
        data = get_data(cheltuiala)
        luna = data[3] + data[4]
        if nr_ap not in rezultat:
            rezultat[nr_ap] = {}
            rezultat[nr_ap]['luna'] = luna
            rezultat[nr_ap]['suma'] = suma
        else:
            if luna in rezultat[nr_ap]['luna']:
                rezultat[nr_ap]['suma'] = rezultat[nr_ap]['suma'] + suma
            else:
                rezultat[nr_ap]['luna'] = luna
                rezultat[nr_ap]['suma'] = suma
    return rezultat