# https://www.phptravels.net/
# http://automationpractice.com/index.php
# https://formy-project.herokuapp.com/
# https://the-internet.herokuapp.com/
# https://www.techlistic.com/p/selenium-practice-form.html
# jules.app
#
# (obs: nu 3 pe fiecare pagina, 3 in total, de pe ce site doriti, la alegere. Nu toate sites vor avea elemente cu atributul name de ex)
#
# 3 selectors by:
# Id
# Link text
# Partial link text
# Name
# Tag*
# Class name*
# Css (1 dupa id, 1 dupa clasa, 1 dupa atribut=valoare_partiala)
#
# *La tag si class name veti folosi find elementS! - salvati in lista. Interactionati cu un element la alegere din lista
#
# La Xpath:
# 3 dupa atribut valoare
# 3 dupa textul de pe element
# 1 dupa partial text
# 1 cu SAU, folosind pipe |
# 1 cu *
# 1 in care le iei ca pe o lista de xpath si in python ajunge 1 element, deci cu (xpath)[1]
# 1 in care sa folosesti parent::
# 1 in care sa folosesti fratele anterior sau de dupa (la alegere)
# 1 functie ca si cea de la clasa prin care sa pot alege eu prin param cu ce element vreau sa interactionez.
#
# Studiu extra daca doriti:
# https://www.automatetheplanet.com/most-exhaustive-xpath-locators-cheat-sheet/
#
#
# 3 selectors by:
# Id

# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# ------------------------------------Selectors by ID ---------------------------------------------
# navigam catre un url
# chrome.get('https://the-internet.herokuapp.com/login')
#
# # 1
# username = chrome.find_element(By.ID, 'username')
# username.send_keys('didris05')

# # 2
# password = chrome.find_element(By.ID, 'password')
# password.send_keys('123')

# navigam catre un url
# chrome.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')

# # 3
# email_create = chrome.find_element(By.ID, 'email_create')
# email_create.send_keys('isabela.didraga@gmail.com')

# ------------------------------------Selectors by Link Text ---------------------------------------
# 1
# chrome.get('https://www.phptravels.net/')
# chrome.find_element(By.LINK_TEXT, 'Blog').click()

# # 2
# chrome.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
# chrome.find_element(By.LINK_TEXT, 'Contact us').click()

# # 3
# chrome.get('https://formy-project.herokuapp.com/')
# chrome.find_element(By.LINK_TEXT, 'Checkbox').click()
#
# ------------------------------------Selectors by Partial Link Text---------------------------------
# # 1
# chrome.get('https://formy-project.herokuapp.com/')
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'Press').click()

# # 2
# chrome.get('https://www.phptravels.net/')
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'Sign').click()

# # 3 => pe exemplu asta mereu primesc eroare pentru ca de fiecare data cand intru pe link, trebuie sa bifez ca sunt de acord cu Recommended Cookies
# chrome.get('https://www.techlistic.com/')
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'Class and Object?').click()

# ------------------------------------Selectors by Name ---------------------------------------
# # 1
# chrome.get('http://automationpractice.com/index.php')
# chrome.find_element(By.NAME, 'search_query').send_keys('Bluza')

# # 2
# chrome.get('https://www.phptravels.net/signup')
# chrome.find_element(By.NAME, 'phone').send_keys('0760131653')

# # 3
# chrome.get('http://automationpractice.com/index.php')
# chrome.find_element(By.NAME, 'email').send_keys('isabela.didraga@gmail.com')

# ------------------------------------Selectors by Tag -------------------------------------
# # 1
# chrome.get('https://www.phptravels.net/login')
# input_list = chrome.find_elements(By.TAG_NAME, 'input')
# input_list[0].send_keys('ddr.isa')
# input_list[1].send_keys('123')

# # 2
# chrome.get('https://formy-project.herokuapp.com/form')
# input_list = chrome.find_elements(By.TAG_NAME, 'Input')
# input_list[0].send_keys('Isa')
# input_list[1].send_keys('Didraga')
# input_list[2].send_keys('Tester')

# # 3
# chrome.get('http://automationpractice.com/index.php?controller=contact')
# chrome.find_element(By.TAG_NAME, 'textarea').send_keys('Multumim!')

# ------------------------------------Selectors by Class Name -------------------------------------

# aici primesc eroarea 'list index out of range........idk why :(('
# # 1
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_elements(By.CLASS_NAME, 'form-control pac-target-input')[1].send_keys('Timisoara')
# chrome.find_elements(By.CLASS_NAME, 'form-control pac-target-input')[2].send_keys('Electronicii')

# # 2
# # 3

# ------------------------------------Selectors by CSS -------------------------------------
# # 1 dupa ID
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.CSS_SELECTOR, 'input#autocomplete').send_keys('Isa')

# # 2 dupa clasa
# chrome.get('https://www.phptravels.net/signup')
# chrome.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('Isa')

# # 3 atribut=valoare_partiala
# chrome.get('https://www.phptravels.net/signup')
# chrome.find_element(By.CSS_SELECTOR, 'input[placeholder*="Last"]').send_keys('Didraga')

# -----------------------XPATH-----------------------------------------------------------------
# # 3 dupa atribut valoare
# chrome.get('https://www.phptravels.net/signup')
# chrome.find_element(By.XPATH, '//input[@name="first_name"]').send_keys('Isabela')
# chrome.find_element(By.XPATH, '//input[@placeholder="Last Name"]').send_keys('Didraga')
# chrome.find_element(By.XPATH, '//input[@type="password"]').send_keys('07')

# # 3 dupa textul de pe element
# chrome.get('http://automationpractice.com/index.php')
# chrome.find_element(By.XPATH, '//a[text()="Best Sellers"]').click()
# chrome.find_element(By.XPATH, '//a[text()="Contact us"]').click()

# # 1 dupa partial text
# chrome.get('https://www.phptravels.net/blog')
# full_text = chrome.find_element(By.XPATH, '//a[contains(text(), "Independent Cultures")]').text # => aici nu pot da click?
# print(full_text)

# # 1 cu SAU, folosind pipe |
# chrome.get('https://www.phptravels.net/login')
# chrome.find_elements(By.XPATH, '//input[@name="email"]|//a[@name="email"].send_keys(isabela.didraga@gmail.com)')

# # 1 cu *
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.XPATH, '//*[@id="autocomplete"]').send_keys('ok')

# # 1 in care le iei ca pe o lista de xpath si in python ajunge 1 element, deci cu (xpath)[1]

# # 1 in care sa folosesti parent::
# chrome.get('https://formy-project.herokuapp.com/form')
# chrome.find_element(By.XPATH, '//label[text()="Job title"]/parent::strong')

# # 1 in care sa folosesti fratele anterior sau de dupa (la alegere)
# chrome.get('https://formy-project.herokuapp.com/form')
# chrome.find_element(By.XPATH, '//label[text()="Job title"]/parent::strong/following-sibling::input')

# # 1 functie ca si cea de la clasa prin care sa pot alege eu prin param cu ce element vreau sa interactionez.
# def formy_input_by_name(name, input_value):
#     input = chrome.find_element(By.XPATH, f'//input[@name="{name}"]')
#     input.send_keys(input_value)
#
# formy_input_by_name('continents', 'Africa' )

sleep(4)
chrome.quit()
