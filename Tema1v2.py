# a. Usor (recomandat)
# 1. Revizualizeaza intalnirea 1 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video cu Variabile si Tipuri de date din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video cu Operatori si Flow Control din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/

# b. Usor spre Mediu (obligatoriu)
# 1.
# In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila
# O variabila este o zona din memorie care tine date

# 2.
# Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri:
# string, int, float, bool
# Valorile le alegeti voi dupa preferinte
# nume = 'Isabela' # String
# varsta = 26 # Int
# inaltime = 1.64 # Float
# casatorita = False # boolean

# print(f'Numele meu este {nume} si am varsta de {varsta} ani, inaltimea de {inaltime} m.')
# print(f'Casatorita: {casatorita}')
#
# 3.
# Utilizat functia type pentru a verifica daca au tipul de date asteptat
# print(type(nume)) # => String
# print(type(varsta)) # => int
# print(type(inaltime)) # => float
# print(type(casatorita)) # => boolean

# sau alta varianta

# if type(nume) == str:
#     print('Variabile nume este de tipul string')

# 4.
# Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
# Verificati tipul acesteia

# inaltime_rotunjita = round(inaltime)
# inaltime = inaltime_rotunjita
# print(f'Inaltimea rotunjita este {inaltime_rotunjita}.')  # => 2
# print(type(inaltime_rotunjita)) # => int

# 5.
# folositi print() si printati in consola 4 propozitii folosind cele 4 variabile.
# (rezolvati nepotrivirile de tip prin ce modalitate doriti)

# print(f'Numele meu este {nume} si am varsta de {varsta} ani, inaltimea de {inaltime} m.')
# print(f'Casatorita: {casatorita}')

# if casatorita == True:
#     print(f'Numele meu este {nume} si am varsta de {varsta} ani, inaltimea de {inaltime} m si sunt casatorita.')
# else:
#     print(f'Numele meu este {nume} si am varsta de {varsta} ani, inaltimea de {inaltime} m si NU sunt casatorita.')

# 6.
# citeste de la tastatura numele
# citeste de la tastatura prenumele
# afiseaza 'Numele complet are x caractere'

# numele = input('Alege un nume: ')
# prenumele = input('Alege un prenume: ')
# print('Numele complet are ', len(numele) + len(prenumele), 'caractere.')

# 7.
# citeste de la tastatura lungimea
# lungimea = int(input('Introduceti lungimea:'))

# citeste de la tastatura latimea
# latimea = int(input('Introduceti latimea: '))

# afiseaza 'Aria dreptunghiului este x'
# aria = lungimea * latimea

# print(f'Aria dreptunghiului este {aria}')

# 8.
# Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
# cititi de la tastatura un int x
# afiseaza stringul fara ultimele x caractere
# ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'

# my_string = 'Coral is either the stupidest animal or the smartest rock'
# x = int(input('Introduceti un numar: '))

# size = len(my_string)
# print(my_string[ : size - x])

# 9.
# acelasi string
# declara un string nou care sa fie format din primele 5 caractere + ultimele 5

# my_string = 'Coral is either the stupidest animal or the smartest rock'
# size = len(my_string)
# print(my_string[ : 4] + my_string[size - 5:])

# 10.
# acelasi string
# afisati de cate ori apare cuvantul 'the'

# my_string = 'Coral is either the stupidest animal or the smartest rock'
# print(my_string.count('the'))

# 11.
# acelasi string
# inlocuieste the cu THE peste tot
# printeaza rezultatul

# my_string = 'Coral is either the stupidest animal or the smartest rock'
# print(my_string.replace(' the',' THE'))

# 12.
# acelasi string
# salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
# (hint: este o functie care te ajuta sa faci asta)

# my_string = 'Coral is either the stupidest animal or the smartest rock'
# index_cuvant = my_string.index('rock')
# print(index_cuvant)

# folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
# print(my_string[:index_cuvant])

# output: 'Coral is either the stupidest animal or the smartest '

# 13.
# citeste de la tastatura un string
# my_string = str.casefold(input('introdu un cuvant: '))

# verifica daca primul si ultimul caracter sunt la fel
# size = len(my_string)

# se va folosi un assert
# assert my_string[:1] == my_string[size-1:size]

# atentie: se doreste ca programul sa fie case insensitive
# 'apA' e acceptat

# 14.
# avand stringul '0123456789'
# my_string = '0123456789'

# afisati doar numerele pare
# nr_par = my_string[2 : : 2]
# print(nr_par)

# acum afisati doar numerele impare
# (hint: folositi slicing, controlati din pas)
# nr_impar = my_string[1 : : 2]
# print(nr_impar)

# 15.
# acelasi string de la 12
# my_string = 'Coral is either the stupidest animal or the smartest rock'

# folositi un assert ca sa verificati daca acest string contine doar numere
# hint: merge cu slicing? probabil ca nu... ce mai stim atunci legat de string?
# poate gasim o functie ajutatoare
# assert  my_string.isdigit() == True

# c. Optionale (may need google)
# 16.
# citeste de la tastatura un string de dimensiune impara
# my_str = input('Introduceti stringul de dimensiune impara: ')

# afiseaza caracterul din mijloc
# size = len(my_str)
# x = int((size + 1) /2)
# middle_char = my_str[x - 1]
# print(f'Caracterul din mijloc este {middle_char}')

# 17.
# Folosind assert, verificati daca un string este palindrom
# my_str = input('Introdu un cuvant: ')
# assert my_str == my_str[: :-1]

# 18.
# folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')
#my_string = input('Introdu un string: ')

# si salveaza fiecare cuvant intr-o variabila
#for word in my_string.split():
#    print(word)
# acum printeaza ambele variabile pentru verificare

# 19.
# citeste un string de la tastatura (eg: alabala portocala)
# str = input('introdu string: ')

# salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite)
# first_char = str[0]
# print(first_char)

# capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
# size = len(str)
# middle = str[1:size-1]
# print(middle)
# => alAbAlA portocAla

# 20.
# citeste un user de la tastatura
# citeste o parola
# afiseaza: 'Parola pt user x este ***** si are x caractere'
# ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
# eg: parola abc => ***
# parola abcd => ****

# user = input('introdu user: ')
# password = input('introdu parola: ')
# hidden_password = '*' * len(password)
# print(f'parola pentru userul {user} este {hidden_password} si are {len(password)} caractere.')