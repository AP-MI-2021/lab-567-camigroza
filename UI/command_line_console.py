from Logic.CRUD import adauga_cheltuiala, sterge_cheltuiala, modifica_cheltuiala
from UI.console import show_all


def help():
    print("Daca doriti sa adaugati o cheltuiala, tastati in primul rand 'add', iar mai apoi,"
          "despartite printr-o virgula si fara spatii intre ele: "
          "id-ul, numarul apartamentului, suma, data si tipul")
    print("Daca doriti sa stergeti o cheltuiala, tastati in primul rand 'delete', iar mai apoi "
          "id-ul cheltuielii pe care doriti sa o stergeti")
    print("Daca doriti sa modificati o cheltuiala, tastati in primul rand 'update', iar mai apoi,"
          "despartite printr-o virgula si fara spatii intre ele: "
          "id-ul, numarul apartamentului, suma, data si tipul")
    print("Daca doriti sa introduceti mai multe comenzi deodata, dati valorile asa cum este specificat mai sus,"
          "iar intre doua comenzi diferite, va rog tastati ';'")
    print("Daca doriti sa va opriti, tastati 'stop'")


def menu(lista):
    ajutor = input("If you need help, type 'help': ")
    if ajutor == 'help':
        help()
    while True:
        given_string = input("Dati comenzile: ")
        all_commands = given_string.split(';')
        stop = 0
        for i in range(len(all_commands)):
            command = all_commands[i]
            command = command.split(',')
            if command[0] == 'add':
                id = int(command[1])
                nr_ap = int(command[2])
                suma = float(command[3])
                data = command[4]
                tip = command[5]
                lista = adauga_cheltuiala(id, nr_ap, suma, data, tip, lista)
            elif command[0] == 'delete':
                id = int(command[1])
                lista = sterge_cheltuiala(id, lista)
            elif command[0] == 'update':
                id = int(command[1])
                nr_ap = int(command[2])
                suma = float(command[3])
                data = command[4]
                tip = command[5]
                lista = modifica_cheltuiala(id, nr_ap, suma, data, tip, lista)
            elif command[0] == 'showall':
                show_all(lista)
            elif command[0] == 'stop':
                stop = 1
        if stop == 1:
            break