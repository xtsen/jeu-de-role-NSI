from random import randint
import os

# import class
from modules import Player as P
from modules import Fighter as F
from modules import Trader as T

"""
    LP : life points
    EVT + event = événement
"""
class Tray:

    """
        Une class Tray qui prend 2 argument pour chaque objet
        max : 1 objet par partie
        param : player, fighter
    """
    def __init__(self, player, fighter, world, day):
        self.__letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.__lenX = world + 6
        self.__lenY = world + 6
        self.__history = []
        self.__day = day

        # formater la date
        dayDisplay = str(self.__day//10) + str(self.__day)[-1]
        day = ["J" + dayDisplay, 0, 0]
        self.__history.append(day)


        # Création du plateau
        self.__Tray = []
        for x in range(self.__lenX):
            newX = []
            for y in range(self.__lenY + 1):
                newX.append(self.__letters[x] + str(y))

            self.__Tray.append(newX)

        self.__world = world
        self.__coordX = 0
        self.__coordY = 0
        self.__Room = Room(player, fighter, self)

    #=============================
    # Les getters
    #=============================  
    def getTray(self):
        """Renvoie le list Tray"""
        return self.__Tray

    def getRoom(self):
        """Renvoie l'objet Room"""
        return self.__Room

    def getX(self):
        """Renvoie l'ordonnée des coordonées"""
        return self.__coordX

    def getY(self):
        """Renvoie l'abcisse des coordonées"""
        return self.__coordY

    def getWorld(self):
        """Renvoie le numero du monde"""
        return self.__world

    def bottomBar(self):
        """Créer l'affichage d'une barre"""
        print("╠═════╬", end='')
        for i in range(self.__lenX - 2):
            print("═════╬", end='')
        print('═════╣')

    def getLenX(self):
        """Renvoie la hauteur du plateau"""
        return self.__lenX

    def getLenY(self):
        """Renvoie la largeur du plateau"""
        return self.__lenY

    def getHistory(self):
        """Renvoie l'historique des déplacements"""
        return self.__history

    def getDay(self):
        """Renvoie le jour actuel"""
        return self.__day

    #=============================
    # Les events
    #=============================  
    def launchRoom(self):
        """Création d'un événement dans l'objet Room"""
        Room.launchEvent(self.__Room)

    def showTray(self, coordX, coordY):
        """Renvoie l'affichage du plateau"""
        self.__Tray = []
        for x in range(self.__lenX):
            newX = []
            for y in range(1, self.__lenY + 1):
                # self.__letters[x] + str(y)
                newX.append("   ")

            self.__Tray.append(newX)

        for day in self.__history:
            self.__Tray[day[1]][day[2]] = day[0]


        self.__Tray[coordX][coordY] = "-O-"

        print("╔═════╦", end='')
        for i in range(self.__lenX - 2):
            print("═════╦", end='')
        print('═════╗')
        for x in range(self.__lenX):
            newX = []
            for y in range(self.__lenY):
                newX.append(self.__Tray[x][y])

            for coord in newX:
                print("║ " + coord, end=" ")

            if x == self.__lenX -1:
                print(" ->")
                print("╚═════╩", end='')
                for i in range(self.__lenX - 2):
                    print("═════╩", end='')
                print('═════╝')
            else:
                print("║")
                self.bottomBar()


    def upgradeWorld(self):
        """Permet d'augmenter le numero du monde"""
        self.__world += 1

    def newDay(self):
        """Permet d'augmenter le jour"""
        self.__day += 1

    def addDay(self, coordX, coordY):
        """Permet d'afficher correctement les jours"""
        dayDisplay = str(self.__day//10) + str(self.__day)[-1]
        day = ["J" + dayDisplay, coordX, coordY]
        self.__history.append(day)

class Room:
    """
        Une class Room qui prend 2 argument pour chaque objet
        max : 48 objets par partie 
        param : player, fighter
    """
    def __init__(self, player, fighter, currentTray):
        self.__player = player
        self.__fighter = fighter
        self.__Tray = currentTray

    #=============================
    # Les getters
    #=============================  
    def getEvent(self):
        """Renvoie l'événement de l'objet"""
        return self.__nameObject

    #=============================
    # Les events
    #=============================  
    def launchEvent(self):

        """Permet de créer aléatoirement un événement"""

        event = ["nothing", "fight", "food", "money", "trader"]
        self.__nameObject = event[randint(0, 4)]
        if self.__nameObject == "fight":
            print('\nOh non !')
            print('Vous êtes en face à face avec un mercenaire !\n')
            fight(self.__player, self.__fighter)
        elif self.__nameObject == "food":
            print('\nVous avez de la chance, vous venez de découvrir un sac plein de nourriture.\n')
            print('Vous avez gagné 20 points de vie et 10 points de force')
            print("————————————————————————————————————————————————\n")
            P.Player.EVT_findFood(self.__player)
        elif self.__nameObject == "trader":
            print('\nOh !')
            print('Vous êtes face à un marchand !\n')
            print("————————————————————————————————————————————————\n")
            trading(self.__player, self.__Tray)
        elif self.__nameObject == "money":
            print('\nVous avez de la chance, vous venez de découvrir un sac plein d\'argent.\n')
            print('Vous avez gagné 100€')
            print("————————————————————————————————————————————————\n")
            P.Player.EVT_findMoney(self.__player)
        else:
            print("\nTout est calme ici, peut etre un peu trop calme ...")
            print("————————————————————————————————————————————————\n")

# fonction des events

def fight(player, fighter):

    """Permet de faire combattre ou non un mercennaire et le joueur"""

    # Décision d'attaque ou non
    fightOrNot = randint(0, 1)

    if fightOrNot == 0:
        print("Aucun combat n'aura lieu")
    else:
        # ajout d'un nombre de chance
        chanceToWin = randint(10, 20)
        currentLevel =  P.Player.getLevel(player)

        LP_Player = P.Player.getLP(player)
        strength_Player = P.Player.getStrength(player) + chanceToWin

        LP_Fighter = F.Fighter.getLP(fighter)
        strength_Fighter = F.Fighter.getStrength(fighter) - chanceToWin

        while LP_Fighter > 0 and LP_Player > 0:
            LP_Player -= strength_Fighter
            LP_Fighter -= strength_Player

        # Update de l'objet player
        newLevels = chanceToWin*10
        PUT_Player(player, LP_Player, P.Player.getStrength(player), P.Player.getMoney(player) + 100)
        P.Player.upgrade(player, newLevels)
        if currentLevel != P.Player.getLevel(player):

            print(f"Le combat vous a fait gagné {newLevels // 100} niveaux, vous êtes maintenant niveau {P.Player.getLevel(player)}")
            print("—————————————————————————————————————————————————\n")

        if LP_Player <= 0:
            print("Vous avez perdu le combat.")
            print(f"Vous êtes mort.")
            print("—————————————————————————————————————————————————\n")
            
        elif LP_Fighter <= 0:
            print("Vous avez gagné le combat.")
            print(f"Vous avez maintenant {P.Player.getLP(player)} points de vie")
            print("—————————————————————————————————————————————————\n")

def trading(player, currentTray):

    """Permet de marchander avec le marchand"""

    print(f"Vous avez actuellement {P.Player.getMoney(player)}€\n")

    # Demande au joueur si il veut acheter un item
    buyOrNo = input("Voulez vous acheter un item au marchand ?")

    if buyOrNo == "oui":

        # Création d'un objet Trader
        trader = T.Trader()

        # Affichage du shop du marchand
        T.Trader.showItems(trader, Tray.getWorld(currentTray))
        item1, item2, item3 = T.Trader.getItems(trader, Tray.getWorld(currentTray))
        items = [item1, item2, item3]

        # list du prix des item
        itemPrices = [item1[1], item2[1], item3[1]]

        currentMoney = P.Player.getMoney(player)

        # Choix de l'item à acheter
        whichItem = int(input("Quel item voulez vous acheter (1, 2 ou 3): "))
        if whichItem == 10:
            whichItem = input("Quel item voulez vous acheter (1, 2 ou 3): ")
            P.Player.setMoney(player, currentMoney + itemPrices[whichItem-1])


        choicedItem = itemPrices[whichItem-1]

        print(f"Vous avez acheter un item au marchand pour {itemPrices[whichItem-1]}€")

        
        # Update de l'objet Player
        PUT_Player(player, P.Player.getLP(player) + items[whichItem-1][2], P.Player.getStrength(player) + items[whichItem-1][3], currentMoney-choicedItem)
        print(f"Vous avez actuellement {P.Player.getMoney(player)}€\n")
        print(f"Vous avez actuellement {P.Player.getLP(player)} points de vie\n")
        print(f"Vous avez actuellement {P.Player.getStrength(player)} points de force\n")

# Début des définitions de fonction

def movePlayer(player, fighter, currentTray, coordX, coordY):

    """Déplace le joueur sur le plateau"""

    # Choix de la direction à prendre (right, left, top, bottom)
    direction = input(f"Que voulez vous faire {P.Player.getName(player)} (acceder au menu taper 'menu') : ")

    if direction == "menu":
        showMenu("inGame")
        movePlayer(player, fighter, currentTray, coordX, coordY)

    elif direction == "top" and coordX != 0:
        coordX -= 1
        
    elif direction == "bottom" and coordX != Tray.getLenX(currentTray) - 1:
        coordX+= 1

    elif direction == "left" and coordY != 0:
        coordY -= 1

    elif direction == "right" and coordY != Tray.getLenX(currentTray) - 1:
        coordY += 1

    elif direction == "save":
        save(player, coordX, coordY, currentTray)
        print("\n—————————————————————————————————————————————————")
        print("Votre partie a bien été sauvegarder")
        print("—————————————————————————————————————————————————")
        movePlayer(player, fighter, currentTray, coordX, coordY)

    elif direction == "profil":
        showProfile(player)
        movePlayer(player, fighter, currentTray, coordX, coordY)

    # Cheatcode
    elif direction == "tp":
        coordX = Tray.getLenX(currentTray)-1
        coordY = Tray.getLenY(currentTray)-2

    # Devcode
    elif direction == "money":
        P.Player.EVT_findMoney(player)
        movePlayer(player, fighter, currentTray, coordX, coordY)

    elif direction == "food":
        P.Player.EVT_findFood(player)
        movePlayer(player, fighter, currentTray, coordX, coordY)

    elif direction == "fight":
        fight(player, fighter)
        movePlayer(player, fighter, currentTray, coordX, coordY)

    elif direction == "trading":
        trading(player, currentTray)
        movePlayer(player, fighter, currentTray, coordX, coordY)

    elif direction == "devmode":
        PUT_Player(player, 300, 100, 1000)
        movePlayer(player, fighter, currentTray, coordX, coordY)

    else:
        print("Vous ne pouvez pas prendre cette direction")
        movePlayer(player, fighter, currentTray, coordX, coordY)

    # return des nouvelles coordonnées
    return coordX, coordY

def round(currentTray, player, tray, currentX, currentY):

    """"Règle l'affiche et met a jour les attributs de l'objet Tray et Player"""

    print("\n—————————————————————————————————————————————————")
    print(f"Vous etes sur la case : {tray[currentX][currentY+1]}")

    # Affichage du plateau
    Tray.showTray(currentTray, currentX, currentY)
    Tray.newDay(currentTray)
    Tray.addDay(currentTray, currentX, currentY)

    # Création d'un objet Room()
    Tray.launchRoom(currentTray)
    player_LP = P.Player.getLP(player)
    player_Strength = P.Player.getStrength(player)
    player_Money = P.Player.getMoney(player)

    PUT_Player(player, player_LP, player_Strength, player_Money)

    return player, currentX, currentY

def PUT_Player(player, LP, Strength, Money):

    """Permet de mettre a jour les attribut de l'objet Player"""

    # une fonction pour update l'objet player
    P.Player.setLP(player, LP)
    P.Player.setStrength(player, Strength)
    P.Player.setMoney(player, Money)

def verif(currentTray, coordX, coordY, player, fighter):
    """Verifie si le joueur est toujours en vie et si il n'est pas sur la dernière case"""
    if coordX == Tray.getLenX(currentTray) - 1 and coordY == Tray.getLenY(currentTray) - 1:

        newWorld(currentTray, player, fighter)

        return False, "reachEnd"
        

    elif P.Player.getLP(player) <= 0:
        return False, "noLP"

    else:
        return True, "OK"

def newWorld(currentTray, player, fighter):
    """Gère la transition entre les mondes"""
    print("Voulez vous passer au niveau suivant ?") 
    wantToContinue = input() 

    if wantToContinue == "oui":
        lastLP = F.Fighter.getLP(fighter)
        lastStrength = F.Fighter.getStrength(fighter)
        fighter = F.Fighter(lastLP + 50, lastStrength + 20)
        lastWorld = Tray.getWorld(currentTray)

        day = Tray.getDay(currentTray)

        newTray = Tray(player, fighter, lastWorld + 1, day)

        coordX = 0
        coordY = 0

        print("Il vous est fortement recommendé de sauvegarder votre partie")
        print("Voulez vous sauvegarder ?")
        wantToContinue = input() 

        newGame(newTray, player, fighter, coordX, coordY)


def end(currentTray, player):

    """Affiche le résumé et notre score"""
    score = (P.Player.getLP(player)*3 + P.Player.getStrength(player)*2 + P.Player.getMoney(player)*2)*P.Player.getDifficulty(player)*P.Player.getLevel(player)*(Tray.getWorld(currentTray))
    writeScore(score)
    writeUsername(P.Player.getName(player))
    print("≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠")
    print(f"\nBravo, {P.Player.getName(player)} vous avez reussi à traverser ce monde !\n")
    print("Profil :")
    print("————————————————————————————————————————————————")
    print(f"• Niveau {P.Player.getLevel(player)}\n")
    print(f"• Vie : {P.Player.getLP(player)}")
    print(f"• Force : {P.Player.getStrength(player)}")
    print(f"• Argent : {P.Player.getMoney(player)}€\n")
    print(f"• Monde : n°{Tray.getWorld(currentTray)}\n")
    print(f"• Total : {score} points")
    print("————————————————————————————————————————————————")

def newGame(currentTray, player, fighter, coordX, coordY):

    """Permet de gérer une partie"""

    tray = Tray.getTray(currentTray)
    canContinue = True

    print(f"Bienvenue dans le monde n°{Tray.getWorld(currentTray)}")

    print("\n—————————————————————————————————————————————————")
    print(f"Vous etes sur la case : {tray[coordX][coordY + 1]}")

    Tray.showTray(currentTray, coordX, coordY)

    while canContinue != False:

        # verif si le joueur à toujours de la vie et si il n'est pas sur la dernière case
        canContinue, reason = verif(currentTray, coordX, coordY, player, fighter)

        if canContinue != False:
        
            coordX, coordY = movePlayer(player, fighter, currentTray, coordX, coordY)

            player, coordX, coordY = round(currentTray, player, tray, coordX, coordY)

    if reason == "reachEnd":
        end(currentTray, player)

    elif reason == "noLP":
        print("Oh non ! vous n'avez plus de vie vous ne pouvez donc pas continuer le jeu.\n")
        deleteSave(player)

def dashboard(currentTray, player, fighter, coordX, coordY):

    """Agis comme un menu, permet de se balader et eventuellement faire des réglages"""

    # Affichage d'un menu
    showMenu("beggining")

    choice = input()

    if choice == "carte":
        Tray.showTray(currentTray, coordX, coordY)
        dashboard(currentTray, player, fighter, coordX, coordY)

    elif choice == "profil":
        print(f"\nProfil de {P.Player.getName(player)} :")
        print("————————————————————————————————————————————————")
        print(f"• Vie : {P.Player.getLP(player)}")
        print(f"• Force : {P.Player.getStrength(player)}")
        print(f"• Argent : {P.Player.getMoney(player)}€\n")
        print("————————————————————————————————————————————————")
        dashboard(currentTray, player, fighter, coordX, coordY)

    elif choice == "événements":
        print(f"{P.Player.getName(player)}, dans ce monde vous pourrez tomber sur 4 événements différents.\n")
        print("Vous pourrez tomber sur un mercenaire qui vous fera perdre de la vie.")
        print("————————————————————————————————————————————————")
        print("Vous pourrez tomber sur de la nourriture qui vous fera gagner de la vie et de la force.")
        print("————————————————————————————————————————————————")
        print("Vous pourrez tomber sur un marchand a qui vous pourrez acheter des items.")
        print("————————————————————————————————————————————————")
        print("Vous pourrez tomber sur un trésor a qui vous fera gagner de l'argent.\n")
        dashboard(currentTray, player, fighter, coordX, coordY)

    elif choice == "difficulté":
        print("Le niveau de difficulté est par défaut à 1 mais vous pouvez le mettre jusqu'au niveau 3.\n")
        difficultyLevel = int(input("Niveau de difficulté désiré : "))
        P.Player.setDifficulty(player, difficultyLevel)
        dashboard(currentTray, player, fighter, coordX, coordY)

    elif choice == "info":

        print("————————————————————————————————————————————————")
        print(f"Pour ce jeu, {nbLines()} lignes de code ont été nécessaire.")
        dashboard(currentTray, player, fighter, coordX, coordY)

    elif choice == "start":
        newGame(currentTray, player, fighter, coordX, coordY)  

    else:
        print("Choix non valide veuillez recommencez") 
        dashboard(currentTray, player, fighter, coordX, coordY)

def initGame():

    """Permet d'initialiser une nouvelle partie"""

    alreadyLogged = input("Avez vous une partie sauvegardé : ")

    if alreadyLogged == "skip":
        player = P.Player(100, 25, 100, "")
        fighter = F.Fighter(100, 20)
        currentTray = Tray(player, fighter, 1, 0)
        coordX = Tray.getX(currentTray)
        coordY = Tray.getY(currentTray)
        dashboard(currentTray, player, fighter, coordX, coordY)

    elif alreadyLogged == "reset":
        deleteData()

    elif alreadyLogged == "oui":
        username = input("Quel étais votre username : ")
        player, coordX, coordY = log(username)

        fighter = F.Fighter(100, 20)
        currentTray = Tray(player, fighter, 1, 0)

    else:
        print("\nBonjour à toi nouveau joueur !")
        username = input("Comment t'appeles tu : ")

        # Création de l'objet player
        player = P.Player(100, 25, 100, username)
        
        print("————————————————————————————————————————————————")
        print(f"Bienvenue dans le monde meconnu et magique de Vendée, le meilleur score est {highestScore()}.\n")
        print("Malheureusement vous avez été téléporté ici par erreur par un magicien qui convoite votre fortune.\n")
        print("Le sorcier vous a laissé comme seule chance de vous en sortir une carte avec la sortie du royaume.")
        print("————————————————————————————————————————————————")
        print("A vous de jouer !\n")
        fighter = F.Fighter(100, 20)
        currentTray = Tray(player, fighter, 1, 0)
        coordX = Tray.getX(currentTray)
        coordY = Tray.getY(currentTray)

    print("————————————————————————————————————————————————")
    input("Taper sur n'importe quelle touche pour continuer ")
    print("————————————————————————————————————————————————\n")

    dashboard(currentTray, player, fighter, coordX, coordY)

# Fonctions pour editer ou lire du texte

def highestScore():
    """
        Fonction qui recupère le meilleur score
    """

    with open('storage/bestScores.txt', "r") as file:
        scores = file.readlines()

        bestScore = 0
        
        for score in scores:
            if int(score) > bestScore:
                bestScore = int(score)
    
    return bestScore

def writeScore(newScore):
    """
        Fonction qui recupère et écrit le nouveau score
    """
    with open('storage/bestScores.txt', "r") as file:
        lines = file.readlines()

        scores = []
        
        for score in lines:
            scores.append(score)

    scores.append(newScore)
    scores.append("\n")

    with open('storage/bestScores.txt', "w") as file:
        for score in scores:
            file.write(f"{score}")

def writeUsername(username):
    """
        Fonction qui recupère et écrit le nouveau joueur
    """
    with open('storage/players.txt', "r") as file:
        lines = file.readlines()

        users = []
        
        for user in lines:
            users.append(user)

    users.append(username)
    users.append("\n")
    

    with open('storage/players.txt', "w") as file:
        for user in users:
            file.write(f"{user}")

def save(player, coordX, coordY, currentTray):

    """Sauvegarde les infos du joueur sur un doc texte"""
    username = P.Player.getName(player)
    level = P.Player.getLevel(player)
    LifePoints = P.Player.getLP(player)
    Strength  = P.Player.getStrength(player)
    Money = P.Player.getMoney(player)
    Difficulty = P.Player.getDifficulty(player)
    World = Tray.getWorld(currentTray)

    infos = [username, level, LifePoints, Strength, Money, Difficulty, coordX, coordY, World]
    with open(f"saves/{username}.txt", "a") as file:
        for info in infos:
            file.write(f"{info}")
            file.write("\n")

    P.Player.saved(player)

def deleteSave(player):
    """Permet de supprimer la sauvegarde de la partie du joueur"""
    # delete backup if exist one
    username = P.Player.getName(player)
    if P.Player.getSaves(player):
        os.remove(f"saves/{username}.txt")

def log(username):
    """Permet de récupérer les infos du joueur a partir d'un doc"""
    with open(f'saves/{username}.txt', "r") as file:
        lines = file.readlines()

        infos = []
        
        for info in lines:
            infos.append(info)

    player = P.Player(int(infos[2]), int(infos[3]), int(infos[4]), infos[0], int(infos[1]))

    P.Player.setDifficulty(player, int(infos[4]))

    return player, int(infos[5]), int(infos[6])

def showProfile(player):
    """Affiche le profil sans le score"""
    print(f"\nProfil de {P.Player.getName(player)} :")
    print("————————————————————————————————————————————————")
    print(f"• Vie : {P.Player.getLP(player)}")
    print(f"• Force : {P.Player.getStrength(player)}")
    print(f"• Argent : {P.Player.getMoney(player)}€\n")
    print("————————————————————————————————————————————————")

def showMenu(mode):
    """Affiche le menu (les commandes possibles)"""
    print("≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠\n")

    if mode == "inGame":
        print("Se deplacer à droite, tapez 'right'")
        print("————————————————————————————————————————————————")
        print("Se deplacer à gauche, tapez 'left'")
        print("————————————————————————————————————————————————")
        print("Se deplacer vers bas, tapez 'bottom'")
        print("————————————————————————————————————————————————")
        print("Se deplacer vers le haut, tapez 'top'")
        print("————————————————————————————————————————————————")
        print("Sauvegarder sa partie, tapez 'save'")
        print("————————————————————————————————————————————————")

    print("Voir la carte, tapez 'carte'")
    print("————————————————————————————————————————————————")
    print("Voir votre profil, tapez 'profil'")
    print("————————————————————————————————————————————————")

    if mode == "beggining":
        print("Voir ce qui vous attends, tapez 'événements'")
        print("————————————————————————————————————————————————")
        print("Définir le niveau de diffuculté, tapez 'difficulté'")
        print("————————————————————————————————————————————————")
        print("Avoir plus d'info, tapez 'info'")
        print("————————————————————————————————————————————————")

    print("Arreter le jeu, maintenez 'ctrl' + 'C'")
    print("————————————————————————————————————————————————")
    print("Commencer le jeu, tapez 'start'")
    print("\n≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠")

def deleteData():
    """Permet de supprimer toutes les données sauvegarder du jeu"""
    sure = input("Êtes vous sûr de cette manoeuvre : ")

    if sure == "oui":

        with open('storage/players.txt', "w") as players:
            players.write("")

        with open('storage/bestScores.txt', "w") as scores:
            scores.write("")

def nbLines():
    """Compte le nombre de lignes de code"""
    nbLines = 0
    with open('main.py') as main:
        lines = main.readlines()
        
        for line in lines:
            nbLines += 1

    with open('modules/Fighter.py') as fighter:
        lines = fighter.readlines()
        
        for line in lines:
            nbLines += 1

    with open('modules/Player.py') as player:
        lines = player.readlines()
        
        for line in lines:
            nbLines += 1

    with open('modules/Trader.py') as trader:
        lines = trader.readlines()
        
        for line in lines:
            nbLines += 1

    return nbLines



initGame()

"""
Prochaine feature : 

    • 
"""