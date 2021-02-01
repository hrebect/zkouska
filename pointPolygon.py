#Určení, zda bod leží uvnitř polygonu
#Tomáš Hřebec ,III. BFGG
#zimní semestr 2020/21
#Úvod do programování

import sys, math
class Point:
#Class, která nese informaci o souřadnicích bodů
#Dále jsou zde gettery, settery a reprezentace bodu
    def __init__ (self,x=0,y=0):
            self.__x=x
            self.__y=y

    def print(self):
        print(self.__x,self.__y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y
    
    def __repr__(self):
        return str(self.__x) + " " + str(self.__y)

class Polygon:
#Class, která nahraje list bodů a z něj vytvoří polygon definovaný těmito body

    def __init__(self, points):
        self.__points = points

    #funkce pro získání hran polygonu. Hrany jsou definované okrajovými body
    @property
    def edges(self):
        edge_list = []
        for i,p in enumerate(self.__points):
            p1 = p
            p2 = self.__points[(i+1) % len(self.__points)]
            edge_list.append((p1,p2))
        return edge_list

    def __repr__(self): #polygon je reprezentovan jako list bodů, které ho tvoří
        return str(self.__points)
    

    #funkce pro zjištění úhlů polygonu a zjištění, zda je konvexní, když není, ukončí program   
    def konvex(self):
        uhly = []
        for i,p in enumerate(self.__points):
            p1 = p
            p2 = self.__points[(i+1) % len(self.__points)]
            p3 = self.__points[(i+2) % len(self.__points)]
            angle = math.degrees(math.atan2(p3.y-p2.y, p3.x-p2.x) - math.atan2(p1.y-p2.y, p1.x-p2.x))
            if angle < 0:
                angle += 360
            uhly.append(angle)
            if all(i > 180 for i in uhly):
                sys.exit(input('Polygon není konvexní.Stistknete ENTER pro ukonceni'))
    
    #funkce na pro určení, zda je hledaný bod uvnitř, či vně polygonu. Hledaný bod vstupuje jako point
    def contains(self, point):
        list_result = []
        for edge in self.edges: 
            result = (point.y - edge[0].y) * (edge[1].x - edge[0].x) - (point.x - edge[0].x) * (edge[1].y - edge[0].y) #vektorový součin
            list_result.append(result)
        
        return all(i <= 0 for i in list_result) #když jsou všechny, čísla záporná, nebo nula, tak vod je uvnitř 


#nacteni bodů do class Point, první bod v txt souhoru je nacten zclášť jako zkoumaný bod, zbytek do listu, který definuje polygon   
alist=[]
try:
    with open('vstup_polygon.txt',encoding="UTF-8") as f:
        bod_str = (f.readline()).rstrip()
        bod_split = bod_str.split()
        bod_int = list(map(int, bod_split))
        bod = Point(bod_int[0],bod_int[1])
        for line in f:
            coord_str = line.rstrip()
            coord_split = coord_str.split()
            coord_int = list(map(int, coord_split))
            alist.append(Point(coord_int[0],coord_int[1]))
           
except FileNotFoundError: #ukonceni programu, kdyz soubor nebude nalezen
    sys.exit(input('Soubor se vstupem nenalezen, měl by mít název "vstup_polygon.txt". Stistknete ENTER pro ukonceni'))
except PermissionError:
    sys.exit(input('Program nemá oprávnění číst soubor se vstupem, stistknete ENTER pro ukonceni'))
except ValueError: #ukoneceni pri nevalidním vstupu
    sys.exit(input('Vstupní soubor obsahuje nepodporovaný formát čísel, stistknete ENTER pro ukonceni'))

q = Polygon(alist)

q.konvex()

#ukladani do .txt souboru
with open('vystup_polygon.txt',mode='w',encoding="UTF-8") as e:
    if q.contains(bod):
        e.write('Bod je uvnitř polygonu')
    else:
        e.write('Bod je mimo polygon')