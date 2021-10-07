from random import randint
class Trader:

    """
        Une class Trader qui ne prend pas d'argument
        max : 48 objets par partie
        param : ø
    """
    def __init__(self):
        items = [
            ["Bouclier", 200, 20, 0],
            ["Épée", 300, 0, 20],
            ["Armure", 300, 50, 0],
            ["Refuge", 400, 50, 30],
            ["Sortilège", 500, 100, 30],
            ["Compagnon", 600, -50, 50]
        ]
        self.__item1 = items[randint(0, len(items)-1)]
        self.__item2 = items[randint(0, len(items)-1)]
        self.__item3 = items[randint(0, len(items)-1)]

    #=============================
    # Les getters
    #=============================  
    def getItems(self, world):
        """Renvoie les items généré aléatoirement"""
        self.updatePrices(world)
        return self.__item1, self.__item2, self.__item3

    def getPrices(self, world):
        """Renvoie les prix de tous les items généré"""
        self.updatePrices(world)
        return self.__item1[1], self.__item2[1], self.__item3[1]

    #=============================
    # Les events
    #=============================  
    def updatePrices(self, world):
        """Augmente le prix des items selon le numero de monde"""
        increase = (world-1)*100
        self.__item1[1] += increase
        self.__item2[1] += increase
        self.__item3[1] += increase

    def showItems(self, world):
        """Affiche le shop du marchand"""
        self.updatePrices(world)
        print("====================")
        print(f"{self.__item1[0]} pour {self.__item1[1]}€")
        print("====================")
        print(f"{self.__item2[0]} pour {self.__item2[1]}€")
        print("====================")
        print(f"{self.__item3[0]} pour {self.__item3[1]}€")
        print("====================\n")
