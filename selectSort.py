#Řazení posloupnosti metodou select sort
#Tomáš Hřebec ,III. BFGG
#zimní semestr 2020/21
#Úvod do programování

import sys

def sort(alist,method):
#sort sequence that is loaded as input parametr alist in list format and it is sorted ascending or descending depending on method 
    for i in range(len(alist)): 
        min_max = i
        for j in range(i+1, len(alist)): #comparison of current position with remaining positions in sequence and saves min or max
            p = comp(alist[min_max],alist[j],method)
            
            if p == alist[min_max]: 
                continue
            min_max = j
        alist[i] , alist[min_max] = alist[min_max] , alist[i] #swapping the current position and the found minimum
    return alist

def comp(a,b,method):
#returns min or max from a,b depending on method
    if method == 'VZ':
        return min(a,b)
    elif method == 'SE':
        return max(a,b)

def metoda(): 
#selection of sorting method. Returns method in string format
    method = input('Zadejta zda chcete posloupnost seřadit vzestupně či sestupně. Pro vzsetupně napište VZ, pro sestupně SE: ') #loading of the method by user
    while method != 'VZ' and method != 'SE': #if method was not loaded in correct format, it asks again
        method = input('Zadali jste nesprávný parametr. Pro vzsetupně napište VZ, pro sestupně SE: ')
    return method
        
def vystup(alist): #saves sorted sequence as .txt file
    with open('vystup_posloupnost.txt',mode='w',encoding="UTF-8") as e:
        for i in alist:
            e.write(str(i)+ "\n")
            

#loading of input .txt wile with unsorted sequence
alist=[]

try:
    with open('vstup_posloupnost.txt',encoding="UTF-8") as f:
        for line in f:
            alist.append(float(line.rstrip()))
except FileNotFoundError: #terminates the program when input file is not found
    sys.exit(input('Soubor se vstupem nenalezen, měl by mít název "vstup_posloupnost.txt". Stistknete ENTER pro ukonceni'))
except PermissionError:
    sys.exit(input('Program nemá oprávnění číst soubor se vstupem, stistknete ENTER pro ukonceni'))
except ValueError: #uterminates the program when input is in invalid format
    sys.exit(input('Vstupní soubor obsahuje nepodporovaný formát čísel, stistknete ENTER pro ukonceni'))

method=metoda()
sort(alist,method)
vystup(alist)

