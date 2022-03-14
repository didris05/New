# a. Recomandat (usor)
# 1. Revizualizeaza intalnirea 6 si ia notite in caz ca ti-a scapat ceva
# b. Obligatorii (mediu)
#
# Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei
#
# 1.
# Clasa Cerc
#
# Atribute: raza, culoare
#
# Constructor pt ambele atribute
#
# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()
#
# class Cerc:
#     # fields and constructor
#     def __init__(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#         self.PI = 3.14
#
#     # methods
#     def descriere_cerc(self):
#         print(f'cercul are raza {self.raza} si culoarea {self.culoare}.')
#
#     def aria(self):
#         a = int(self.PI * self.raza * self.raza)
#         print(f'Aria cercului este {a}.')
#
#     def diametru(self):
#         d = 2 * self.raza
#         print(f'Diametruel cercului este {d}.')
#
#     def circumferinta(self):
#         c = 2 * self.PI * self.raza
#         print(f'Circumferinta cercului este {c}.')
#
# cerc1 = Cerc(3, 'alb')
# cerc2 = Cerc(4, 'gri')
# print('')
# cerc1.descriere_cerc()
# cerc2.descriere_cerc()
# print('')
# cerc1.aria()
# cerc2.aria()
# print('')
# cerc1.diametru()
# cerc2.diametru()
# print('')
# cerc2.circumferinta()
# cerc1.circumferinta()

# 2.
# Clasa Dreptunghi
#
# Atribute: lungime, latime, culoare
#
# Constructor pt toate atributele
#
# Metode:
# descrie()
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare.
# Puteti verifica schimbarea culorii prin apelarea metodei descrie().

# class Dreptunghi:
#     # fields and constructor
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     # methods
#     def descriere(self):
#         print(f'Dreptunghiul are lungimea de {self.lungime} cm, latimea de {self.latime} cm si este {self.culoare}.')
#
#     def aria(self):
#         print(f'Aria dreptunghiului este {self.lungime * self.latime}.')
#
#     def perimetrul(self):
#         print(f'Perimetrul dreptunghiului este {2 * (self.lungime + self.latime)}.')
#
#     def schimba_culoare(self, culoare):
#         self.culoare = culoare
#         print(f'Noua culoare este {self.culoare}')
#
# dreptunghi1 = Dreptunghi(5, 20, 'negru')
# dreptunghi2 = Dreptunghi(6, 4, 'gri')
# print('')
# dreptunghi1.descriere()
# dreptunghi2.descriere()
# print('')
# dreptunghi1.aria()
# dreptunghi2.aria()
# print('')
# dreptunghi1.perimetrul()
# dreptunghi2.perimetrul()
# print('')
# dreptunghi1.schimba_culoare('rosu')
# dreptunghi1.descriere()

# 3.
# Clasa Angajat
#
# Atribute: nume, prenume, salariu
#
# Constructor pt toate atributele
#
# Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)
#
# class Angajat:
#     # fields and constructor
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     # methods
#     def descriere(self):
#         print(f'Angajatul cu numele {self.nume} lucreaza la compania X si are un salariu de {self.salariu} EURO.')
#
#     def nume_complet(self):
#         print(f'Angajatul se numeste {self.nume} {self.prenume}.')
#
#     def salariu_lunar(self):
#         print(f'Angajatul are un salariul lunar de {self.salariu} EURO.')
#
#     def salariu_anual(self):
#         print(f'Angajatul are un salariul anual de {self.salariu * 12} EURO.')
#
#     def marire_salariu(self, marire):
#         self.marire = marire
#         self.salariu = int((self.marire / 100 * self.salariu) + self.salariu)
#         print(f'Salariul dupa marire este de {self.salariu} EURO.')
#
# angajat1 = Angajat('Mitica', 'Ion', 1200)
# angajat2 = Angajat('Popescu', 'Ana', 3000)
# print('')
# angajat1.descriere()
# angajat2.descriere()
# print('')
# angajat1.nume_complet()
# angajat2.nume_complet()
# print('')
# angajat1.salariu_lunar()
# angajat2.salariu_lunar()
# print('')
# angajat1.salariu_anual()
# angajat2.salariu_anual()
#
# angajat1.marire_salariu(25)
# angajat2.marire_salariu(35)
#
# 4.
# Clasa Factura
#
# Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
#
# Constructor: toate atributele, fara serie
#
# Metode:
# schimba_cantitatea(cantitate)
# schimba_pretul(pret)
# schimba_nume_produs(nume)
# genereaza_factura() - va printa tabelar daca reusiti
#
# Factura seria x numar y
# Data: generati automat data de azi
# Produs | cantitate | pret bucata | Total
# Telefon |      7       |       700       | 49000

# import TableIt
# from datetime import date

# class Factura:
#     # fields
#     # fuuny comment: daca las date reale, imi plateste cineva factura?:))
#
#
#     # constructor
#     def __init__(self, numar, nume_produs, cantitate, pret_buc):
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#
#     # methods
#     def schimba_cantitatea(self, cantitate):
#         self.cantitate = cantitate
#         print(f'Noua cantitate este {self.cantitate} buc.')
#
#     def schimba_pretul(self, pret_buc):
#         self.pret_buc = pret_buc
#         print(f'Noul pret este {self.pret_buc} RON.')
#
#     def schimba_nume_produs(self, nume_produs):
#         self.nume_produs = nume_produs
#         print(f'Noul nume al produsului este {self.nume_produs}.')
#
#     def genereaza_factura(self):
#         SERIA = 'FR350'
#         print(f'Factura cu seria {SERIA} si numarul {self.numar}')
#         print(f'Data: {date.today()}')
#         self.my_list = [
#             ['nume', 'cantitate', 'pret buc', 'total'],
#             [self.nume_produs, self.cantitate, self.pret_buc, (self.cantitate * self.pret_buc)]
#         ]
#         TableIt.printTable(self.my_list, useFieldNames = True)
#
# factura1 = Factura(123, 'paine', 3, 5)
# factura1.genereaza_factura()
# factura1.schimba_nume_produs('mere')
# factura1.schimba_cantitatea(50)
# factura1.schimba_pretul(150)
# factura1.genereaza_factura()

# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/
# 5.
# Clasa Cont
#
# Atribute: iban, titular_cont, sold
#
# Constructor pentru toate
#
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)

# class Cont:
#
#     def __init__(self, iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#
#     def afisare_sold(self):
#         print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')
#
#     def debitare_cont(self, suma_debit):
#         self.suma_debit = suma_debit
#         self.sold = self.sold + self.suma_debit
#
#     def creditare_cont(self, suma_credit):
#         self.suma_credit = suma_credit
#         if self.sold > self.suma_credit:
#             self.sold = self.sold - self.suma_credit
#         else:
#             print('Nu poti accesa suma ceruta.')
#
#
# cont1 = Cont(1234, 'Didraga', 3500)
# cont1.afisare_sold()
# print('')
# cont1.debitare_cont(500)
# cont1.afisare_sold()
# print('')
# cont1.creditare_cont(4000)
# cont1.afisare_sold()


# BONUS: (daca aveti timp si doriti sa lucrati suplimentar)
#
# 6.
# Clasa Masina
#
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate masinile cand ies din fabrica sunt gri
# Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
# Culori disponibile = alegeti voi 5-7 culori
# Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
# Inmatriculata = False
#
# Constructor: model, viteza_maxima
#
# Metode:
# descrie() (se vor printa toate atributele, inafara de culori_disponibile)
# inmatriculare() - va schimba atributul inmatriculata in True
# vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
# accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
# franeaza() - masina se va opri si va avea viteza 0

# class Masina:
#
#     marca = 'Audi'
#     model = None
#     viteza_maxima = None
#     viteza_actuala = 0
#     culoare = 'gri'
#     culori_disponibile = {'alb', 'negru', 'rosu', 'gri', 'albastru'}
#     inmatriculata = False
#
#     def __init__(self, model, viteza_maxima):
#         self.model = model
#         self.viteza_maxima = viteza_maxima
#
#     def descriere(self):
#         print(f'Masina este marca {self.marca}, modelul {self.model}, are o viteza maxima de {self.viteza_maxima} Km/h.')
#         print(f'Viteza actuala este {self.viteza_actuala} si are culoarea {self.culoare}.')
#         if self.inmatriculata == False:
#             print('Masina nu este inmatriculata.')
#         else:
#             print('Masina este inmatriculata.')
#
#     def inmatriculare(self):
#         self.inmatriculata = True
#         print('Masina este inmatriculata acum.')
#
#     def vopsire(self, culoare):
#         if culoare in self.culori_disponibile:
#             self.culoare = culoare
#             print(f'Masina a fost vopsita {self.culoare}')
#         else:
#             print(f'Culoarea {culoare} nu este disponibila.')
#
#     def accelerare(self, viteza):
#         self.viteza_actuala = viteza
#         if self.viteza_actuala == 0:
#             print('Masina sta pe loc, nu ai accelerat. Ai introdus viteza 0.')
#         elif self.viteza_actuala < 0:
#             print('Masina nu poate accelera la o viteza negativa.')
#         elif self.viteza_actuala < self.viteza_maxima:
#             print(f'Masina a ccelerat pana la viteza de {self.viteza_actuala} km/h.')
#         else:
#             print(f'Maina nu poate merge cu o viteza mai mare de {self.viteza_maxima}')
#
#     def franeaza(self):
#         self.viteza_actuala = 0
#         print('Masina este orpita')
#
# masina1 = Masina('A4', 350)
# masina1.descriere()
# print('')
# masina1.inmatriculare()
# masina1.descriere()
# print('')
# masina1.vopsire('verde')
# masina1.descriere()
# print('')
# masina1.vopsire('alb')
# masina1.descriere()
# print('')
# masina1.accelerare(250)
# masina1.descriere()
# print('')
# masina1.franeaza()
# masina1.descriere()

# 7. Clasa TodoList
#
#
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor
#
# Metode:
# adauga_task() - se va adauga in dict
# finalizeaza_task() - se va sterge din dict
# afiseaza_todo_list() - doar cheile
# afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare
# daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
# Daca acesta raspunde nu - la revedere
# daca raspunde da - il cerem detalii task si salvam nume+detalii in dict

# class TodoList:
#
#     todo = {
#
#
#     }
#
#     def adauga_task(self):
#         self.todo['cumparaturi'] = 'Nu uita ce cumparaturi.'
#         self.todo['rezervare'] = 'Rezerva camera pentru excursie.'
#         self.todo['telefon'] = 'Suna-ti mama.'
#
#     def finalizeaza_task(self, task):
#         self.task = task
#
#         if self.task in self.todo:
#             self.todo.pop(self.task)
#             print(f'Task-ul {self.task} a fost finalizat.')
#         else:
#             print(f'Task-ul {self.task} nu este in lista.')
#
#     def afiseaza_todo_list(self):
#         print(self.todo.keys())
#
#     def afiseaza_todo(self):
#         for key, value in self.todo.items():
#             print(key, ':', value)
#
#     def afiseaza_detalii_suplimentare(self, new_task):
#         self.new_task = new_task
#         self.raspuns = None
#         self.detalii = None
#         if self.new_task not in self.todo:
#             print('Task-ul nu este in lista,vrei sa il adaugi?')
#             self.raspuns = input('Scrieti raspunsul (da/nu): ')
#             if self.raspuns == 'nu':
#                 print('La revedere')
#             elif self.raspuns == 'da':
#                 print('Scrieti detaliile pentru noul task (nume si detalii')
#                 self.detalii = input('Scrieti detalii: ')
#                 self.todo[new_task] = self.detalii
#             else:
#                 print('Nu ai raspuns cu DA sau NU!!!!')
# todo1 = TodoList()
#
# todo1.afiseaza_todo_list()
# print('')
# todo1.adauga_task()
# todo1.afiseaza_todo()
# todo1.afiseaza_todo_list()
# print('')
# todo1.finalizeaza_task('renovare')
# todo1.finalizeaza_task('cumparaturi')
# todo1.afiseaza_todo()
# print('')
# todo1.afiseaza_todo_list()
# todo1.afiseaza_detalii_suplimentare('manichiura')
# print('')
# todo1.afiseaza_todo_list()
# todo1.afiseaza_todo()