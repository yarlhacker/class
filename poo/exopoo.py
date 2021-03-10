from math import sqrt

class Point:
    def __init__(self,absc,order):
        self.__absc = absc
        self.__order = order

    @property
    def absc(self):
        return self.__absc 

    @absc.setter
    def absc(self,X):
        self.__absc = X

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self,Y):
        self.__order = Y


    def __str__(self):
        return f"({self.absc},{self.order})"

    def calculerdistance(self, p):
        return sqrt(pow(self.absc - p.__absc, 2) + pow(self.order - p.__order,2))


    def calculermilieu(self,p):
        p = Point((self.absc + p.__absc)/2, (self.lsorder + p.__order)/2)
        return p


# p =Point(5,9)
# p1 =Point(3,7)
# print(p.calculermilieu(p1))




class TroisPoint:
    def __init__(self,premier:Point, deuxieme:Point, troisieme:Point) -> bool:
        self.__premier = premier
        self.__deuxieme = deuxieme
        self.__troisieme = troisieme

    @property
    def premier(self):
        return self.__premier

    @premier.setter
    def premier(self,X):
        self.__premier = X 
    
    @property
    def deuxieme(self):
        return self.__deuxieme

    @deuxieme.setter
    def deuxieme(self,Y):
        self.__deuxieme = Y
    @property
    def troisieme(self):
        return self.__troisieme

    @deuxieme.setter
    def deuxieme(self,Z):
        self.__troisieme = Z

    def sont_alignes(self):
        AB = self.premier.calculerdistance(self.deuxieme)
        AC = self.premier.calculerdistance(self.troisieme)
        BC = self.deuxieme.calculerdistance(self.troisieme)

        return AB == AC + BC or AC == AB + BC or  BC == AC + AB
            
    def est_isocele(self):
        AB = self.premier.calculerdistance(self.deuxieme)
        AC = self.premier.calculerdistance(self.troisieme)
        BC = self.deuxieme.calculerdistance(self.troisieme)
        
        return AB == AC or AB == BC or BC == AC

    @staticmethod
    def calculerdistance(p):
        return sqrt(pow(self.absc - p.__absc, 2) + pow(self.order - p.__order,2))

    @staticmethod
    def calculermilieu(p):
        p = Point((absc + p.__absc)/2, (slsorder + p.__order)/2)
        return p
        


t = TroisPoint(Point(8, 5), Point(8, 8), Point(8, 0))

print(t.calculerdistance)