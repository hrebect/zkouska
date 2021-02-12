#Určení, zda bod leží uvnitř polygonu
#Tomáš Hřebec ,III. BFGG
#zimní semestr 2020/21
#Úvod do programování

import sys, math
class Point:
#Class with information about coordinates of points
#getter, setter and representation functions

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
#class that creates polygon from list of points

    def __init__(self, points):
        self.__points = points

    #function to obtain edges of polygon. Edges are defined by edge points
    @property
    def edges(self):
        edge_list = []
        for i,p in enumerate(self.__points):
            p1 = p
            p2 = self.__points[(i+1) % len(self.__points)]
            edge_list.append((p1,p2))
        return edge_list

    def __repr__(self): #polygon is represented as list of points 
        return str(self.__points)
    
    #function to obtain information that polygon is convex or not. If not, program will be stoped
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
        if all(i > 180 for i in uhly) or all(i < 180 for i in uhly): #if is polygon in CCW orientatin, angles are more than 180 degree
            return
        sys.exit(input('Polygon není konvexní.Stistknete ENTER pro ukonceni'))
    
    #function to obtain information that search point is inside or outside. The seatch point enters into funtion like 'point'
    def contains(self, point):
        result_previous = None
        for edge in self.edges: 
            result = (point.y - edge[0].y) * (edge[1].x - edge[0].x) - (point.x - edge[0].x) * (edge[1].y - edge[0].y)
            if result_previous is None:
                result_previous = result
            if result * result_previous <= 0:
                with open('vystup_polygon.txt',mode='w',encoding="UTF-8") as e: 
                    e.write('Bod je mimo polygon')
                return
            result_previous = result
        with open('vystup_polygon.txt',mode='w',encoding="UTF-8") as e:
            e.write('Bod je uvnitř polygonu')

#loading of points from .txt file to class Point. The first point is the search point and remaining points are vertices of polygon  
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
           
except FileNotFoundError:  #terminates the program when input file is not found
    sys.exit(input('Soubor se vstupem nenalezen, měl by mít název "vstup_polygon.txt". Stistknete ENTER pro ukonceni'))
except PermissionError:
    sys.exit(input('Program nemá oprávnění číst soubor se vstupem, stistknete ENTER pro ukonceni'))
except ValueError: #uterminates the program when input is in invalid format
    sys.exit(input('Vstupní soubor obsahuje nepodporovaný formát čísel, stistknete ENTER pro ukonceni'))

q = Polygon(alist)
q.konvex()
q.contains(bod)