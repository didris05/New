# a. Usor (recomandat)
# 1. Revizualizeaza intalnirea 2 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video despre Operatori si Flow Control din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 3 despre Structuri de date din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/
#
# b. Usor spre Mediu (obligatoriu)
# Pentru toate exercitiile se va folosi notiunea de if in rezolvare.
# Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if
# X poate fi initializat direct in cod sau citit de la tastatura, dupa preferinte.
# X este un int
#
# 1.
# Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else
# in cadrul unui if else, se verifica daca conditia din if este indeplinita (si se returneaza rezultatul), iar daca aceasta conditie nu este indeplinita
# codul trece pe ramura de else (si se returneaza rezultatul).

# 2.
# Verifica si afiseaza daca x este numar natural sau nu
# x = int(input('Introduceti un numar: '))
# if x > 0:
#     print('Acesta este un numar natural')
# else:
#     print('Acesta NU este un numar natural')
#
# 3.
# Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
# x = int(input('Introduceti un numar: '))
# if x > 0:
#     print('Acesta este un numar pozitiv.')
# elif x < 0:
#     print('Acesta este un numar negativ.')
# else:
#     print('Acesta este un numar neutru.')
#
# 4.
# Verifica si afiseaza daca x este intre -2 si 13 => nu este specificat daca inclusiv -2 si 13
# x = int(input('Introduceti un numar: '))
# if x > -2 and x < 13:
#     print('Acest numar este curpins intre -2 si 13. ')
# else:  #  aceasta cerinta nu era specificata in exercitiu
#     print('Acest numar nu este cuprins intre -2 si 13')

# 5.
# Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
# x = int(input('Introduceti un numar: '))
# y = int(input('Introduceti un numar: '))
# if x - y < 5:
#     print('Diferenta este mai mica decat 5.')
# 6.
# Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)
# x = int(input('Introduceti un numar: '))
# if not(x > 5 and x < 27):
#     print('Numarul nu este intre 5 si 27.')
#
# 7.
# x si y (int)
# Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
#
# x = int(input('Introduceti un numar: '))
# y = int(input('Introduceti un numar: '))
# if x == y:
#     print('Cele doua numere sunnt egale. => x = y')
# elif x > y:
#     print('Primul numar (x) este mai mare decat al doilea (y). => x > y')
# else:
#     print('Al doilea numar (y) este mai mare decat primul (x). => y > x')

# 8.
# X, y, z - laturile unui triunghi
# Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
# x = int(input('Introduceti un numar: '))
# y = int(input('Introduceti un numar: '))
# z = int(input('Introduceti un numar: '))
# if (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
#     print('Triunghiul este isoscel.')
# elif x == y and x == z and y == z:
#     print('Triunghiul este echilateral.')
# else:
#     print('Triunghiul este oarecare.')

# 9.
# Citeste o litera de la tastatura
# letter = str.casefold(input('Introduceti o litera: '))
#
# Verifica si afiseaza daca este vocala sau nu
# if letter.isdigit():
#     print('Nu ai introdus o litera, ci altceva.')
# elif letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
#     print('Litera este vocala.')
# else:
#     print('Litera nu este vocala.')
#
# 10.
# Transforma si printeaza notele din sistem romanesc in  >
# n = float(input('Introduceti o nota: '))
# Peste 9 => A
# if n > 10:
#    print('Nu a-ti introdus o nota de la 0 la 10.')
# elif n > 9:
#     print('Nota este: A')
# #Peste 8 => B
# elif n > 8:
#     print('Nota este: B')
# #Peste 7 => C
# elif n > 7:
#     print('Nota este: C')
# #Peste 6 => D
# elif n > 6:
#     print('Nota este: D')
# #Peste 4 => E
# elif n > 4 and n < 6:
#     print('Nota este: E')
# #4 sau sub => F
# elif n <= 4 and n > 0:
#     print('Nota este: F')
# else:
#     print('Nu a-ti introdus o nota de la 0 la 10.')

# c. Optionale (may need google)
#
# 11.
# Verifica daca x are minim 4 cifre
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
# x = int(input('Introdu un numar: '))
# if x / 1000 > 1:  #  sau x <= 1000 and x >= 1000
#     print('Numarul are minim patru cifre.')
# else:
#     print('Numarul are mai putin de 4 cifre.')

# 12.
# Verifica daca x are exact 6 cifre
# x = int(input('Introdu un numar: '))
# if x / 100000 > 1 and x / 100000 < 10:
#     print('Numarul are exact 6 cifre.')

# 13.
# Verifica daca x este numar par sau impar
# x = int(input('Introdu un numar: '))
# if x % 2 == 0:
#     print('Numarul este par.')
# else:
#     print('Numarul este impar')

# 14.
# x, y, z (int)
# Afiseaza care este cel mai mare dintre ele?
# x = int(input('Introdu un numar: '))
# y = int(input('Introdu un numar: '))
# z = int(input('Introdu un numar: '))
# if x >= y  and x >= z: #  if a == b == c => egale
#     print(f'{x} este cel mai mare numar')
# elif y >= x and y >= z:
#     print(f'{y} este cel mai mare numar.')
# else:
#     print(f'{z} este cel mai mare numar.')

# 15.
# X, y, z - reprezinta unghiurile unui triunghi
# Verifica si afiseaza daca triunghiul este valid sau nu
# x = int(input('Introduceti masura unui unghi al triunghiului xyz: '))
# y = int(input('Introduceti masura unui unghi al triunghiului xyz: '))
# z = int(input('Introduceti masura unui unghi al triunghiului xyz: '))
# if x + y + z == 180 and x > 0 and y > 0 and z > 0:
#     print('Triunghiul este valid.')
# else:
#     print('Triunghiul nu este valid.')

# Bonus la cerere:
# 16.
# Verificare imbarcare persoane
# Tineti urmatoarele date
# Varsta
# Insotit de mama
# Insotit de tata
# Pasaport
# Act permisiune mama
# Act permisiune tata

# varsta = int(input('Itroduceti varsta: '))
# insotit_de_mama = False
# insotit_de_tata = True
# pasaport = True
# act_permisiune_mama = False
# act_permisiune_tata = True

# Conditii de imbarcare
# Daca pers are varsta peste 18 ani si are pasaport
# if varsta >= 18 and pasaport == True:
#     print('Imbarcare reusita.')
# Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
# elif varsta < 18 and pasaport == True and insotit_de_mama == True and insotit_de_tata == True:
#     print('Imbarcare reusita.')
# Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la celalat parinte
# elif varsta < 18 and pasaport == True and (insotit_de_mama == True and act_permisiune_tata == True) or (insotit_de_tata == True and act_permisiune_mama == True):
#     print('Imbarcare reusita.')
# else:
#     print('Imbarcare nereusita.')

# Aici vreau sa testati codul cu toate variantele posibile
# Sa generati cazuri de test si expected result, apoi sa rulati codul si sa completati actual results
#
# Ex:
# Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
# Varsta 17 ani, am pasaport, doar mama si act permisiune tata => Ma pot imbarca
# Varsta 17 ani, am pasaport, doar tata si act permisiune tata => Nu ma pot imbarca
# Varsta 17 ani, am pasaport, doar mama si act permisiune mama => Nu ma pot imbarca
# Varsta 17 ani, am pasaport, doar tata si act permisiune mama => Ma pot imbarca
# Varsta 17 ani, am pasaport, fara mama si fara tata si act permisiune tata => Nu ma pot imbarca
# Varsta 17 ani, am pasaport, fara mama si fara tata si act permisiune mama => Nu ma pot imbarca
# Varsta 17 ani, am pasaport, fara tata si fara tata si fara act permisiune tata si far act permisiune mama=> Nu ma pot imbarca
#
#
# 17. Joc ghicit zarul
# Cauta pe net si vezi cum se genereaza un numar random
# Ne imaginam ca dam cu zarul si salvam acest numar in dice_roll
# import random
# dice_roll = random.randint(1,6)
#
# Luati un nr ghicit de la utilizator
# x = int(input('Alegeti un numar dat cu zarul, de la 1 la 6: '))
#
# Verificati si afisati daca utilizatorul a ghicit
# 3 optiuni
# Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# if x < dice_roll:
#     print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {x}, dar a fost {dice_roll}.')
#
# Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# elif x > dice_roll:
#     print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {x}, dar a fost {dice_roll}.')
#
# Ai ghicit. Felicitari? Ai ales x si zarul a fost y
# else:
#     print(f'Ai ghicit. Felicitari? Ai ales {x} si zarul a fost {dice_roll}.')
