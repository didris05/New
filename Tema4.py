# a. Usor (recomandat)
# 1. Revizualizeaza intalnirea 4 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video despre Flow Control din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 5 despre Functii din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/
#
# Iteratiile sunt greute, deoarece necesita putina gandire algoritmica
# Va rog sa imi scrieti pe slack unde intampinati dificultati si va ajut
# Daca stati blocati > 30 min, cereti indiciu
#
# b. Dificultate medie (Faceti cat puteti din ele)
#
# # 1.
# # Avand lista
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# #
# # Folositi un for ca sa iterati prin toata lista si sa afisati
# # ‘Masina mea preferata este x’
# for i in range(len(masini)):
#     print(f'Masina mea preferata este {masini[i]}')
#
# # Faceti acelasi lucru cu un for each
# for masina in masini:
#     print(f'Masina mea preferata este {masina}')
# # Faceti acelasi lucru cu un while
# i = 0
# while i <= len(masini)-1:
#     print(f'Masina mea preferata este {masini[i]}')
#     i = i + 1

# 2.
# Aceeasi lista
# Folositi un for else
# In for
#    Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
# In else
#     Printati lista
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# i = 0
# for i in range(len(masini)):
#     masini[i] = masini[i].upper()
#     masini[0] = masini[0].casefold()
#     masini[len(masini)-1] = masini[len(masini)-1].casefold()
# else:
#     print(masini)


# 3.
# Aceeasi lista,
# Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea prin modalitatea aleasa de voi
# Daca masina e mercedes
#    Printam ‘am gasit masina dorita de dvs’
#    Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel
#    Printam Am gasit masina X. Mai cautam
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     if masina == 'Mercedes':
#         print('Am gasit masina dorita de dvs.')
#         break
#     else:
#         print(f'Nu am gasit masina. Mai cautam')
#
# 4.
# Aceasi lista
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun
# Iterati prin lista
#
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# (nu trebuie else)
# Printati S-ar putea sa va placa masina x
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     if masina != 'Lastun' and masina != 'Trabant':
#         print(f'S-ar putea sa va placa masina {masina}')
#         continue
# 5.
# Modernizati parcul de masini
# Creati o lista goala, masini_vechi
# Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# Salvati aceste masini in masini_vechi
# Suprascrieti-le cu ‘Tesla’
# Printati Modele vechi: x
# Modele noi: x
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
# for i in range(len(masini)):
#     if masini[i] == 'Lastun' or masini[i] == 'Trabant':
#         masini_vechi.append(masini[i])
#         masini[i] = 'Tesla'
# else:
#     print(f'Modele vechi: {masini_vechi}')
#     print(f'Masini noi {masini}')
#
#
# 6.
# Avand dict
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina x
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# buget = 15000
# for masina, pret in pret_masini.items():
#     if pret <= buget:
#         print(f'Pentru un buget de sub 15000 euro puteti alege masina {masina}')
#
#
# 7.
# Avand lista
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea
# Afisati de cate ori apare 3
# (nu aveti voie sa folositi count)
# counter = 0
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# for numar in numere:
#     if numar == 3:
#         counter += 1
# print(f'3 apare de {counter} ori')
#
#
# 8. nu stiu daca am voie sa il fac asa?!?!?!
# Aceeasi lista
# Iterati prin ea
# Calculati si afisati suma numerelor
# (nu aveti voie sa folositi sum) => suma este 30
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# s = 0
# for numar in numere:
#     s = s + numar
# print(f'Suma numerelor este {s}')
#
#
# 9.
# Aceeasi lista
# Iterati prin ea
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# for numar in numere:
#     numere.sort()
# print(f'Cel mai mare numar este {(len(numere)-1)}')
#
#
# 10.
# Aceeasi lista
# Iterati prin ea
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista
# i = 0
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# for i in range(len(numere)):
#     if i > 0:
#         numere[i] = -abs(numere[i])
# else:
#     print(numere)
# nu se poate face cu while pentru ca atunci cand il intalneste pe -4 conditia nu mai e indeplinita si ultimul 3 nu il mai face negativ
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# i = 0
# while numere[i] > 0:
#     numere[i] = -abs(numere[i])
#     i += 1
# print(numere)
#
# c. Optionale (may need google)
#
# 11.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Iterati prin lista alte_numere
# Populati corect celelalte liste
# Afisati cele 4 liste la final
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# i = 0
# for i in range(len(alte_numere)):
#     if alte_numere[i] % 2 == 0:
#         numere_pare.append(alte_numere[i])
#     elif alte_numere[i] % 2 != 0:
#         numere_impare.append(alte_numere[i])
#     if alte_numere[i] > 0:
#         numere_pozitive.append(alte_numere[i])
#     else:
#         numere_negative.append(alte_numere[i])
# print(f'Numerele pare sunt {numere_pare}')
# print(f'Numerele impare sunt {numere_impare}')
# print(f'Numerele pozitive sunt {numere_pozitive}')
# print(f'Numerele negative sunt {numere_negative}')
#
#
# 12.
# Aceeasi lista
# Ordonati crescator lista fara sa folositi sort
# Va puteti inspira vizual de aici
# https://www.youtube.com/watch?v=lyZQPjUT5B4
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# for i in range(len(alte_numere)):
#     for j in range(i + 1, len(alte_numere)):
#         if alte_numere[i] > alte_numere[j]:
#             alte_numere[i], alte_numere[j] = alte_numere[j], alte_numere[i]
# print(alte_numere)
#
#
# 13. Nu stiu sa fac cu while !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# Numar_ghicit = None
# Folosind un while
#    User alege un numar
#    Programul ii spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitari! Ai ghicit!
# import random
# numar_secret = random.randint(1,30)
# numar_ghicit = None
# while numar_ghicit == None:
#     nr = int(input('Introdu un numar: '))
#     if nr > numar_secret:
#         print('Numarul este mai mare.')
#     elif nr < numar_secret:
#         print('Numarul este mai mic.')
#     else:
#         print('Felicitari, ai gasit numarul!')
#         break #  daca nu pun break pot sa inserez nr mereu chiar daca eu am ghicit
# # aici cum pot sa fac ca de fiecare data cand introduc un nr sa se genereze un alt random no??
#
# 14.
# Alegeti un numar de la tastatura
# Ex:7
# Scrieti un program care sa genereze in consola urmatoarea piramida
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
#
# Ex:3
# 1
# 22
# 333
#
# x = int(input('Introdu un numar: '))
# for i in range(0,x):
#     for j in range(0, i + 1):
#         print(i + 1, end='')
#     print('\r')
#
#
# 15.
# Iterati prin lista 2d
# Printati ‘Cifra curenta este x’
# (hint: nested for - adica for in for)
# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# for i in range(len(tastatura_telefon)):
#    for j in range(len(tastatura_telefon[i])):
#        print(f'Cifra curenta este {tastatura_telefon[i][j]}')

