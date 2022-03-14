# '''
# 1.Display the sum of 5 + 10, using two variables: x and y.
# x = 5
# y = 10
# print(f'Suma este: {x + y}')

# 2. Creați cȃte o variabilă de tipul: string, int și float, după cum urmează:
# Variabila de tip int va reține valoarea 20.
# x = int(20)
# print(x)
# Variabila de tip float va reține valoarea 10.
# y = float(10)
# print(y)
# Variabila de tip string reține valoarea "python".
# z = 'python'
# print(z)

# 3. Utilizȃnd funcția type, determinați tipul următoarelor variabile:
# restanta = 0
# print(type(restanta)) #  => int
#
# notaFinala = 10.0 #  => float
# print(type(notaFinala)) #  => int
#
# laborator = "Introducere in informatica" #  => string
# print(type(laborator)) #  => int

# 4. Verificaţi dacă un cuvânt este palindrom. Un cuvânt este palindrom dacă scris de la dreapta la
# stanga, este tot acel cuvânt.(folositi assert pt verificare)
# cuvant = input('Introdu un cuvant: ')
# assert cuvant == cuvant[: :-1]

# 5. Remove first n characters from a string (n il cititi de la tatatura)
# "Ana are mere" daca n=3 va afisa " are mere"
# str = input('introduceti un string: ')
# n = int(input('Introdu cate caractere sa fie sterse: '))
# print(str[n : ])

# 5.reads two numbers and multiplies them together and print out their product
# x = int(input('Introdu un numar: '))
# y = int(input('Introdu un numar: '))
# print(f'Produsul este: {x * y}')

# 6.Check if the first and last number of a string  is the same stringul il cititi de la tastatura
# str = input('Introdu un string: ')
# assert str[0] == str[-1]

# 7. Write a program to find how many times substring "Emma" appears in the given string.
# str_x = "Emma is good developer. Emma is a writer"
# print(f'Emma apare de {str_x.count("Emma")} ori.')

# 8. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# pt "eu merg la mare" sa imi afiseze "eure"
# my_str = 'eu merg la mare'
# size = len(my_str)
# print(my_str[ : 2] + my_str[size - 2:])

# 9. Write a Python program to calculate the length of a string.
# pt "eu merg la mare" ->15
# my_str = 'eu merg la mare'
# print(f'Lungimea stringului este: {len(my_str)} caractere.')

# 10. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
# except the first char itself. Go to the editor
# Sample String : 'restart'
# Expected Result : 'resta$t'
# my_str = 'restart'
# print(my_str[0] + my_str[1::].replace('r', '$'))

# 11. Utilizand tipurile de print pe care vi le-am aratat:
# afisati in consola I have 1000 dollars so I can buy 3 football for 450.00 dollars.
# pt datele
# totalMoney = 1000
# quantity = 3
# price = 450
# print(f'I have {totalMoney} dollars so I can buy {quantity} football for {price}.00 dollars')

# 12.Build a program to calculate the followings using the input from the user for a, b, c or r
# • triangle area using input
# import math
#
# a = int(input('Introdu lungimea laturii: '))
# b = int(input('Introdu lungimea laturii: '))
# c = int(input('Introdu lungimea laturii: '))
# p = (a + b + c) / 2
# area = '{:.2f}'.format(cmath.sqrt(p * (p - a) * (p - b) * (p - c)))
# print(f'Aria triunghiului este: {area}')

# • rectangle area and perimeter
# a = int(input('Introdu lungimea: '))
# b = int(input('Introdu latimea: '))
# print(f'Perimetrul este {a +b}')
# print(f'Aria este {a * b}')

# • circle area
# r = int(input('Introdu raza: '))
# PI = 3.14
# print(f'Aria cercului cu raza de {r} este {PI * r * r}')

# 13. Which of the following are valid ways to specify the string literal foo'bar in Python:
# 'foo\'bar' #  => merge
# """foo'bar""" #  => merge
# "foo'bar" #  => merge
# 'foo''bar' #  => NU merge
# 'foo'bar' #  => NU merge

# 14.Password checker script
# Define a username getting input from the console
# Define a password getting input from the console
# Display the following message 'The password for user Paul is
# ********* is 9 characters long)
# username = input('Introdu username: ')
# password = input('Introdu parola: ')
# hidden_password = '*' * len(password)
# print(f'The password for {username} is {hidden_password} and is {len(password)} characters long.')

# de cautat pe net:
# 15.Write a program to take three names as input from a user in the single input() function call.
# name1, name2, name3 = input('Introdu nume: ').split()
# print(f'Primul nume este {name1}, al doilea nume este {name2} si al treilea nume este {name3}')

# 16. Display float number with 2 decimal places
# no_float = 3.14159
# formatted_float = "{:.2f}".format(no_float)
# print(formatted_float)
