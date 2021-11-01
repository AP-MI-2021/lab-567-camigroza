from Logic.CRUD import adauga_cheltuiala, sterge_cheltuiala, modifica_cheltuiala
from UI.console import show_all


def help():
    print("Daca doriti sa adaugati o cheltuiala, tastati in primul rand 'add', iar mai apoi,"
          "despartite printr-o virgula si fara spatii intre ele:"
          "id-ul, numarul apartamentului, suma, data si tipul")
    print("Daca doriti sa stergeti o cheltuiala, tastati in primul rand 'delete', iar mai apoi "
          "numarul apartamentului pentru care doriti sa stergeti cheltuiala")
    print("Daca doriti sa modificati o cheltuiala, tastati in primul rand 'update', iar mai apoi,"
          "despartite printr-o virgula si fara spatii intre ele:"
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
        for i in range(len(all_commands)):
            command = all_commands[i]
            command = command.split(',')
            if command[0] == 'add':
                id = command[1]
                nr_ap = command[2]
                suma = command[3]
                data = command[4]
                tip = command[5]
                lista = adauga_cheltuiala(id, nr_ap, suma, data, tip, lista)
            elif command[0] == 'delete':
                nr_ap = int(command[1])
                lista = sterge_cheltuiala(nr_ap, lista)
            #elif command[0] == 'update':
                #id = command[1]
                #nr_ap = command[2]
                #suma = command[3]
                #data = command[4]
                #tip = command[5]
                #lista  = modifica_cheltuiala(id, nr_ap, suma, data, tip, lista)
            elif command[0] == 'showall':
                show_all(lista)
            elif command[0] == 'stop':
                break
