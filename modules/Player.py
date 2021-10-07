class Player:

    """
        Une class Player qui prend 4 argument pour chaque objet
        max : 1 objet par partie
        param : LP: int, Strength: int, Money: int, name: str
    """

    def __init__(self, LP, Strength, Money, name):
        self.__Name = name
        self.__LP = LP
        self.__Strength = Strength
        self.__Money = Money
        self.__Difficulty = 1
        self.__Saved = False
        self.__Level = 100

    #=============================
    # Les getters
    #=============================
    def getName(self):
        """Renvoie le nom du joueur"""
        return self.__Name

    def getStrength(self):
        """Renvoie la force du joueur"""
        return self.__Strength

    def getLP(self):
        """Renvoie les points de vie du joueur"""
        return self.__LP

    def getMoney(self):
        """Renvoie le solde du compte en banque du joueur"""
        return self.__Money

    def getDifficulty(self):
        """Renvoie le niveau de difficulté choisi"""
        return self.__Difficulty

    def getSaves(self):
        """Verifie si le joueur a effectué une sauvegarde de sa partie"""
        return self.__Saved

    def getLevel(self):
        """Renvoie le niveau du joueur"""
        return self.__Level // 100

    #=============================
    # Les setters
    #=============================
    def setLP(self, newVal):
        """Permet de changer la valeur de la vie du joueur"""
        self.__LP = newVal

    def setStrength(self, newVal):
        """Permet de changer la valeur de la force du joueur"""
        self.__Strength = newVal

    def setMoney(self, newVal):
        """Permet de changer la valeur de l'argent du joueur"""
        self.__Money = newVal

    def setDifficulty(self, newVal):
        """Permet de régler la force et les points du joueur selon le niveau de difficulté"""
        self.__Difficulty = newVal

        if self.__Difficulty == 2:
            self.__LP = 75
            self.__Strength = 20

        elif self.__Difficulty == 3:
            self.__LP = 50
            self.__Strength = 15
            self.__Money = 0

        elif self.__Difficulty == 50:
            self.__LP = 10
            self.__Strength = 5
            self.__Money = -100

    def saved(self):
        """Permet d'affirmer que le joueur a fait une sauvegarde"""
        self.__Saved = True

    def upgrade(self, LevelPoints):
        """Permet d'augmenter le niveau du joueur"""
        self.__Level += LevelPoints

    #=============================
    # Les events
    #=============================  
    def EVT_findFood(self):
        """Permet d'augmenter la force et la vie du joueur lorsqu'il trouve de la nourriture"""
        self.__LP += 20
        self.__Strength += 10

    def EVT_findMoney(self):
        """Permet d'augmenter lle solde du compte en banque du joueur lorsqu'il trouve de l'argent"""
        self.__Money += 100
