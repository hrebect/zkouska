#Řazení posloupnosti metodou select sort
#Tomáš Hřebec ,III. BFGG
#zimní semestr 2020/21
#Úvod do programování

import sys

def vzestup(alist): 
#seradí posloupnost, která je do funkce nahrána jako vsupní parametr alist ve formátu list.
    for i in range(len(alist)): 
        min_index = i
        for j in range(i+1, len(alist)): #porovnani aktualni pozice se zbyvajicimi pozicemi v posloupnosti, a ulozi si minimum
            if alist[min_index] > alist[j]:
                min_index = j
        alist[i] , alist[min_index] = alist[min_index] , alist[i] #prohozeni aktualni pozice a nalezeneho minima
    return alist

def sestup(alist):
#stejná funkce jako vzestup, ale seřadí posloupnost alist sestupně
    for i in range(len(alist)):
        min_index = i
        for j in range(i+1, len(alist)):
            if alist[min_index] < alist[j]:
                min_index = j
        alist[i] , alist[min_index] = alist[min_index] , alist[i]
    return alist

def metoda(alist): 
#výber zda se bude řadit vzestupně či sestupně. Vstuoní parametr alist je neseřazená posloupnost ve formátu list
    b = input('Zadejta zda chcete posloupnost seřadit vzestupně či sestupně. Pro vzsetupně napište VZ, pro sestupně SE: ') #načtení metody
    while b != 'VZ' and b != 'SE': #kontroluje zda byla zadana metoda korektně, když ne, uživatel zadává znovu
        b = input('Zadali jste nesprávný parametr. Pro vzsetupně napište VZ, pro sestupně SE: ')
    if b == 'VZ': #zavolání funkce sestup nebo vzestup na nesařezanou posloupnost
         vzestup(alist) 
    elif b == 'SE':
        sestup(alist)
    return alist
        
def vystup(alist): #ukladani do .txt souboru
    with open('vystup_posloupnost.txt',mode='w',encoding="UTF-8") as e:
        for i in alist:
            e.write(str(i)+ "\n")
            

#nacžteni vstupniho souboru a ošetření některých singularit
alist=[]

try:
    with open('vstup_posloupnost.txt',encoding="UTF-8") as f:
        for line in f:
            alist.append(float(line.rstrip()))
except FileNotFoundError: #ukonceni programu, kdyz soubor nebude nalezen
    sys.exit(input('Soubor se vstupem nenalezen, měl by mít název "vstup_posloupnost.txt". Stistknete ENTER pro ukonceni'))
except PermissionError:
    sys.exit(input('Program nemá oprávnění číst soubor se vstupem, stistknete ENTER pro ukonceni'))
except ValueError: #ukoneceni pri nevalidním vstupu
    sys.exit(input('Vstupní soubor obsahuje nepodporovaný formát čísel, stistknete ENTER pro ukonceni'))

metoda(alist)
vystup(alist)

