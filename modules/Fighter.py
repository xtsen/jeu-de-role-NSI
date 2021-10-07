from random import randint
class Fighter:

    """
        Une class Fighter qui prend 2 argument pour chaque objet
        max : 48 objets par partie
        param : LP: int, Strength: int, Money: int, name: str
    """
    def __init__(self, LP, Strength):
        self.__LP = LP
        self.__strength = Strength
        self.__level = randint(1, 3)
        self.setFighter()

    #=============================
    # Les getters
    #=============================  
    def getStrength(self):
        """Renvoie la force du mercennaire"""
        return self.__strength

    def getLP(self):
        """Renvoie les points de vie du mercennaire"""
        return self.__LP

    #=============================
    # Les setters
    #============================= 

    # une fonction pour différents niveaux de mercenaires
    def setFighter(self):
        """Permet de régler la force et les points du mercennaire selon le niveau de difficulté"""
        if self.__level == 2:
            self.__LP += 20
            self.__strength += 10

        elif self.__level == 3:
            self.__LP += 40
            self.__strength += 20
