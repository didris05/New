# a. Usor (recomandat)
# 1. Revizualizeaza intalnirea 3 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video despre Structuri de date din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 4 despre Flow Control din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/
#
# b. Usor spre Mediu (obligatoriu)
#
# # 1.
# # Declara o lista note_muzicale in care sa pui do re mi etc pana la do
# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
#
# # Afiseaz-o
# print(f'Lista cu note muzicale este: {note_muzicale}')
#
# # Inverseaza ordinea folosind slicing si suprascrie aceasta lista
# # Printeaza varianta actuala (inversata)
# print(f'Lista inversata este: {note_muzicale[::-1]}')
#
# # Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
# # Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
# reversed(note_muzicale)
# print(f'Lista inversata folosind reversed este: {note_muzicale}')
# #
# # Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi intr-o lista noua. Metoda gasita de tine, face suprascrierea automat si permanentizeaza aceste modificari. Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.
# #
# # 2.
# # De cate ori apare ‘do’?
# print(f'Do apare de {note_muzicale.count("do")} ori.')
#
# # 3.
# # Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
#
# # Gasiti 2 variante sa le uniti intr-o singura lista.
# # lista3 = lista1 + lista2
# # print(f'Prima varianta folosind adunare: {varianta1}')
# lista3 = lista1.__add__(lista2)
# print(f'A doua varianta folosind add: {lista3}')
#
# # Afisati lista ordonata astfel [0,1,2,3,4,5,6]
# lista3_ordonata = sorted(lista3)
# print(f'Varianta 1 ordonata: {lista3_ordonata}')
#
# lista3_ordonata = sorted(lista3)
# print(f'Varianta 2 ordonata: {lista3_ordonata}')
#
# #
# # 4.
# # Sortati si afisati lista generata la ex anterior
# sorted(lista3)
# print(f'Lista sortata este: {lista3}')
#
# # Stergeti numarul 0 folosind o functie
# # Afisati iar lista
# while 0 in lista3:
#     lista3.remove(0)
# print(f'Lista fara elementul 0 este: {lista3}')
# #
# # 5.
# # Folosind un if verificati lista generata la ex3 si afisati
# # Lista este goala
# # Lista nu este goala
# if len(lista3) == 0:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')
# #
# # 6.
# # Folositi o functie care sa stearga lista de la ex3
# lista3.clear()
# print(lista3)
# #
# # 7.
# # Copy paste la ex 5. Verificati inca o data.
# # Acum ar trebui sa se afiseze ca lista e goala
# if len(lista3) == 0:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')

# # 8.
# # Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# # Folositi o functie ca sa afisati Elevii (cheile)
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(dict1.keys())
#
# # 9.
# # Printati cei 3 elevi si notele lor
# # Ex: ‘Ana a luat nota {x}’
# # Doar nota o veti lua folosindu-va de cheie
#
# print(f'Ana a luat nota {dict1.get("Ana")}. Gigel a luat nota {dict1.get("Gigel")}. Dorel a luat nota {dict1.get("Dorel")}.')
#
# # 10.
# # Dorel a facut contestatie si a primit 6
# # Modificati nota lui Dorel in 6
# dict1['Dorel'] = 6
#
# # Printati nota dupa modificare
# print(f'Dorel si-a marit nota la {dict1.get("Dorel")}')
# # 11.
# # Gigel se transfera din clasa
# # Cautati o functie care sa il stearga
# dict1.pop('Gigel')
#
# # Vine un coleg nou. Adaugati Ionica, cu nota 9
# dict1['Ionica'] = 9
#
# # Printati noii elevi
# print(dict1)
# #
# # 12.
# # Set
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# # Adaugati in zilele_sapt ‘luni’
# zile_sapt.update(weekend)
# print(zile_sapt)
# # Afisati zile_sapt
# #
# # 13.
# # Folositi un if si verificati daca
# # Weekend este un subset al zilelor din sapt
# # Weekend nu este un subset al zilelor din sapt
# if weekend.issubset(zile_sapt):
#     print('Weekend este un subset al zilelor din sapt')
# else:
#     print('Weekend nu este un subset al zilelor din sapt')
# #
# # 14.
# # Afisati diferentele dintre aceste 2 seturi
# print(zile_sapt.difference(weekend))
#
# # 15.
# # Afisati intersectia elementelor din aceste 2 seturi
# print(zile_sapt.intersection(weekend))
#
# c. Optionale (may need google)
#16
# Declara o Lista cu 5 jucatori
# Schimbari_efectuate = va jucati voi cu valori diferite
# schimbari_max = 3
#
# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
# Efectuam schimbarea
# Stergem jucatorul scos din lista
# Adaugam jucatorul intrat
# Afisam a intra x, a iesit y, mai aveti z schimbari
# Daca jucatorul nu e in teren:
# Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# Afisati ‘mai aveti z schimbari’

SCHIMBARI_MAXIME = 3
schimbari_efectuate = 2
# calculam si initializam schimbari ramase
schimbari_ramase = SCHIMBARI_MAXIME - schimbari_efectuate
echipa = {'j1', 'j2', 'j3', 'j4', 'j5'}
jucator_in = 'j6'
jucator_out = 'j1'

# daca jucatorul e in tere SI daca mai am schimbari
if jucator_out in echipa and schimbari_ramase > 0:
    if jucator_in in echipa: # eliminam cazul cand jucatorul este deja in teren
        print('Nu putem face schimbarea deoarece jucatorul introdus este deja in teren')
    else: # cazul valid, facem tot ce trebuie facut
        echipa.remove(jucator_out)  # scoatem jucatorul
        echipa.add(jucator_in)  # adaugam jucatorul nou
        schimbari_ramase = schimbari_ramase - 1  # contorizam schimbarea
        print(f'Schimbare efectuata cu succes!')
        print(f'A intrat {jucator_in}, a iesit {jucator_out}, mai aveti {schimbari_ramase} schimbari')
else:
    if schimbari_ramase <= 0:
        print('Nu mai ai schimbari')
    else:
        print(f'Nu se poate efectua schimbarea deoarece jucatorul {jucator_out} nu e in teren')
print(f'Actuala echipa este {echipa}')

# caz1 jucator adaugat deja in teren => nu se face sch {'j1', 'j5', 'j3', 'j4', 'j2'}
# caz2 jucator scos nu este in teren => nu se face sch {'j1', 'j5', 'j3', 'j4', 'j2'}
# caz3 happy flow, cand putem face sch, jucator in nu e in teren, jucator out e in teren {'j4', 'j6', 'j2', 'j5', 'j3'}
# caz4 nu mai am schimbari => nu mai am schimbari {'j1', 'j5', 'j3', 'j4', 'j2'}

# Google search hint
# “how to check if item is in list python”
#

