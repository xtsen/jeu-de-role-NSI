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
        return self.__Name

    def getStrength(self):
        return self.__Strength

    def getLP(self):
        return self.__LP

    def getMoney(self):
        return self.__Money

    def getDifficulty(self):
        return self.__Difficulty

    def getSaves(self):
        return self.__Saved

    def getLevel(self):
        return self.__Level // 100

    #=============================
    # Les setters
    #=============================
    def setLP(self, newVal):
        self.__LP = newVal

    def setStrength(self, newVal):
        self.__Strength = newVal

    def setMoney(self, newVal):
        self.__Money = newVal

    def setDifficulty(self, newVal):
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
        self.__Saved = True

    def upgrade(self, LevelPoints):
        self.__Level += LevelPoints

    #=============================
    # Les events
    #=============================  
    def EVT_findFood(self):
        self.__LP += 20
        self.__Strength += 10

    def EVT_findMoney(self):
        self.__Money += 100
