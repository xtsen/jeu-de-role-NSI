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
    def __init__(self, player, fighter):
        tray = [
            ["A1", "A2", "A3", "A4", "A5", "A6", "A7"],
            ["B1", "B2", "B3", "B4", "B5", "B6", "B7"],
            ["C1", "C2", "C3", "C4", "C5", "C6", "C7"],
            ["D1", "D2", "D3", "D4", "D5", "D6", "D7"],
            ["E1", "E2", "E3", "E4", "E5", "E6", "E7"],
            ["F1", "F2", "F3", "F4", "F5", "F6", "F7"],
            ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]
        ]
        self.__coordX = 0
        self.__coordY = 0
        self.__Tray = tray
        self.__Room = Room(player, fighter)

    #=============================
    # Les getters
    #=============================  
    def getTray(self):
        return self.__Tray

    def getRoom(self):
        return self.__Room

    def getX(self):
        return self.__coordX

    def getY(self):
        return self.__coordY

    #=============================
    # Les events
    #=============================  
    def launchRoom(self):
        Room.launchEvent(self.__Room)

    def showTray(self, coordX, coordY):
        tray = [
            ["A1", "A2", "A3", "A4", "A5", "A6", "A7"],
            ["B1", "B2", "B3", "B4", "B5", "B6", "B7"],
            ["C1", "C2", "C3", "C4", "C5", "C6", "C7"],
            ["D1", "D2", "D3", "D4", "D5", "D6", "D7"],
            ["E1", "E2", "E3", "E4", "E5", "E6", "E7"],
            ["F1", "F2", "F3", "F4", "F5", "F6", "F7"],
            ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]
        ]
        self.__Tray = tray
        self.__Tray[coordX][coordY] = "-O-"
        print("————————————————————————————————————")
        print(f"| {self.__Tray[0][0]} | {self.__Tray[0][1]} | {self.__Tray[0][2]} | {self.__Tray[0][3]} | {self.__Tray[0][4]} | {self.__Tray[0][5]} | {self.__Tray[0][6]} |")
        print("————————————————————————————————————")
        print(f"| {self.__Tray[1][0]} | {self.__Tray[1][1]} | {self.__Tray[1][2]} | {self.__Tray[1][3]} | {self.__Tray[1][4]} | {self.__Tray[1][5]} | {self.__Tray[1][6]} |")
        print("————————————————————————————————————")
        print(f"| {self.__Tray[2][0]} | {self.__Tray[2][1]} | {self.__Tray[2][2]} | {self.__Tray[2][3]} | {self.__Tray[2][4]} | {self.__Tray[2][5]} | {self.__Tray[2][6]} |")
        print("————————————————————————————————————")
        print(f"| {self.__Tray[3][0]} | {self.__Tray[3][1]} | {self.__Tray[3][2]} | {self.__Tray[3][3]} | {self.__Tray[3][4]} | {self.__Tray[3][5]} | {self.__Tray[3][6]} |")
        print("————————————————————————————————————")
        print(f"| {self.__Tray[4][0]} | {self.__Tray[4][1]} | {self.__Tray[4][2]} | {self.__Tray[4][3]} | {self.__Tray[4][4]} | {self.__Tray[4][5]} | {self.__Tray[4][6]} |")
        print("————————————————————————————————————")
        print(f"| {self.__Tray[5][0]} | {self.__Tray[5][1]} | {self.__Tray[5][2]} | {self.__Tray[5][3]} | {self.__Tray[5][4]} | {self.__Tray[5][5]} | {self.__Tray[5][6]} |")
        print("————————————————————————————————————")
        print(f"| {self.__Tray[6][0]} | {self.__Tray[6][1]} | {self.__Tray[6][2]} | {self.__Tray[6][3]} | {self.__Tray[6][4]} | {self.__Tray[6][5]} | X |")
        print("————————————————————————————————————")
class Room:
    """
        Une class Room qui prend 2 argument pour chaque objet
        max : 48 objets par partie 
        param : player, fighter
    """
    def __init__(self, player, fighter):
        self.__player = player
        self.__fighter = fighter

    #=============================
    # Les getters
    #=============================  
    def getEvent(self):
        return self.__nameObject

    #=============================
    # Les events
    #=============================  
    def launchEvent(self):
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
            trading(self.__player)
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

    # Décision d'attaque ou non
    fightOrNot = randint(0, 1)

    if fightOrNot == 0:
        print("Aucun combat n'aura lieu")
    else:
        # ajout d'un nombre de chance
        chanceToWin = randint(1, 20)

        LP_Player = P.Player.getLP(player)
        strength_Player = P.Player.getStrength(player) + chanceToWin

        LP_Fighter = F.Fighter.getLP(fighter)
        strength_Fighter = F.Fighter.getStrength(fighter) - chanceToWin

        while LP_Fighter > 0 and LP_Player > 0:
            LP_Player -= strength_Fighter
            LP_Fighter -= strength_Player

        # Update de l'objet player
        PUT_Player(player, LP_Player, P.Player.getStrength(player), P.Player.getMoney(player) + 100)
        if LP_Player <= 0:
            print("Vous avez perdu le combat.")
            print(f"Vous êtes mort.")
            print("—————————————————————————————————————————————————\n")
            
        elif LP_Fighter <= 0:
            print("Vous avez gagné le combat.")
            print(f"Vous avez maintenant {P.Player.getLP(player)} points de vie")
            print("—————————————————————————————————————————————————\n")

def trading(player):
    print(f"Vous avez actuellement {P.Player.getMoney(player)}€\n")

    # Demande au joueur si il veut acheter un item
    buyOrNo = input("Voulez vous acheter un item au marchand ?")

    if buyOrNo == "oui":

        # Création d'un objet Trader
        trader = T.Trader()

        # Affichage du shop du marchand
        T.Trader.showItems(trader)
        item1, item2, item3 = T.Trader.getItems(trader)
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

def movePlayer(player, coordX, coordY):

    # Choix de la direction à prendre (right, left, top, bottom)
    direction = input(f"Que voulez vous faire {P.Player.getName(player)} (acceder au menu taper 'menu') : ")

    if direction == "menu":
        showMenu("inGame")
        movePlayer(player, coordX, coordY)

    elif direction == "top" and coordX != 0:
        coordX -= 1
        
    elif direction == "bottom" and coordX != 6:
        coordX+= 1

    elif direction == "left" and coordY != 0:
        coordY -= 1

    elif direction == "right" and coordY != 6:
        coordY += 1

    # Cheatcode

    elif direction == "save":
        save(player, coordX, coordY)
        print("\n—————————————————————————————————————————————————")
        print("Votre partie a bien été sauvegarder")
        print("—————————————————————————————————————————————————")

    elif direction == "tp":
        coordX = 6
        coordY = 5

    elif direction == "money":
        P.Player.EVT_findMoney(player)
        movePlayer(player, coordX, coordY)

    elif direction == "food":
        P.Player.EVT_findFood(player)
        movePlayer(player, coordX, coordY)

    elif direction == "profil":
        showProfile(player)
        movePlayer(player, coordX, coordY)

    elif direction == "devmode":
        PUT_Player(player, 300, 100, 1000)
        movePlayer(player, coordX, coordY)

    else:
        print("Vous ne pouvez pas prendre cette direction")
        movePlayer(player, coordX, coordY)

    # return des nouvelles coordonnées
    return coordX, coordY

def round(currentTray, player, tray, currentX, currentY):

    print("\n—————————————————————————————————————————————————")
    print(f"Vous etes sur la case : {tray[currentX][currentY]}")

    # Affichage du plateau
    Tray.showTray(currentTray, currentX, currentY)

    # Création d'un objet Room()
    Tray.launchRoom(currentTray)
    player_LP = P.Player.getLP(player)
    player_Strength = P.Player.getStrength(player)
    player_Money = P.Player.getMoney(player)

    PUT_Player(player, player_LP, player_Strength, player_Money)

    return player, currentX, currentY

def PUT_Player(player, LP, Strength, Money):

    # une fonction pour update l'objet player
    P.Player.setLP(player, LP)
    P.Player.setStrength(player, Strength)
    P.Player.setMoney(player, Money)

def verif(coordX, coordY, player):
    if coordX == 6 and coordY == 6:
        return False, "reachEnd"

    elif P.Player.getLP(player) <= 0:
        return False, "noLP"

    else: 
        return True, "OK"

def newGame(currentTray, player, coordX, coordY):

    tray = Tray.getTray(currentTray)
    canContinue = True

    print("\n—————————————————————————————————————————————————")
    print(f"Vous etes sur la case : {tray[coordX][coordY]}")

    Tray.showTray(currentTray, coordX, coordY)

    while canContinue != False:

        # verif si le joueur à toujours de la vie et si il n'est pas sur la dernière case
        canContinue, reason = verif(coordX, coordY, player)

        if canContinue != False:
        
            coordX, coordY = movePlayer(player, coordX, coordY)

            player, coordX, coordY = round(currentTray, player, tray, coordX, coordY)

    if reason == "reachEnd":
        score = (P.Player.getLP(player)*5 + P.Player.getStrength(player)*2 + P.Player.getMoney(player)*2)*P.Player.getDifficulty(player)
        writeScore(score)
        writeUsername(P.Player.getName(player))
        print("≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠")
        print(f"\nBravo, {P.Player.getName(player)} vous avez reussi à traverser ce monde !\n")
        print("Profil :")
        print("————————————————————————————————————————————————")
        print(f"• Vie : {P.Player.getLP(player)}")
        print(f"• Force : {P.Player.getStrength(player)}")
        print(f"• Argent : {P.Player.getMoney(player)}€\n")
        print(f"• Total : {score} points")
        print("————————————————————————————————————————————————")
        deleteSave(player)
    elif reason == "noLP":
        print("Oh non ! vous n'avez plus de vie vous ne pouvez donc pas continuer le jeu.\n")
        deleteSave(player)

def dashboard(currentTray, player, fighter, coordX, coordY):

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

    elif choice == "start":
        newGame(currentTray, player, coordX, coordY)  

    else:
        print("Choix non valide veuillez recommencez") 
        dashboard(currentTray, player, fighter, coordX, coordY)

def initGame():

    alreadyLogged = input("Avez vous une partie sauvegardé : ")

    if alreadyLogged == "skip":
        player = P.Player(100, 25, 100, "")
        fighter = F.Fighter(100, 20)
        currentTray = Tray(player, fighter)
        coordX = Tray.getX(currentTray)
        coordY = Tray.getY(currentTray)
        dashboard(currentTray, player, fighter, coordX, coordY)


    elif alreadyLogged == "oui":
        username = input("Quel étais votre username : ")
        player, coordX, coordY = log(username)

        fighter = F.Fighter(100, 20)
        currentTray = Tray(player, fighter)

    else:
        print("\nBonjour à toi nouveau joueur !")
        username = input("Comment t'appeles tu : ")

        # Création de l'objet player
        player = P.Player(100, 25, 100, username)
        
        print("————————————————————————————————————————————————")
        print(f"Bienvenue dans le monde meconnu et magique de Vendée le meilleur score est {highestScore()}.\n")
        print("Malheureusement vous avez été téléporté ici par erreur par un magicien qui convoite votre fortune.\n")
        print("Le sorcier vous a laissé comme seule chance de vous en sortir une carte avec la sortie du royaume.")
        print("————————————————————————————————————————————————")
        print("A vous de jouer !\n")
        fighter = F.Fighter(100, 20)
        currentTray = Tray(player, fighter)
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

def save(player, coordX, coordY):
    username = P.Player.getName(player)
    LifePoints = P.Player.getLP(player)
    Strength  = P.Player.getStrength(player)
    Money = P.Player.getMoney(player)
    Difficulty = P.Player.getDifficulty(player)

    infos = [username, LifePoints, Strength, Money, Difficulty, coordX, coordY]
    with open(f"saves/{username}.txt", "a") as file:
        for info in infos:
            file.write(f"{info}")
            file.write("\n")

    P.Player.saved(player)

def deleteSave(player):

    # delete backup if exist one
    username = P.Player.getName(player)
    if P.Player.getSaves(player):
        os.remove(f"saves/{username}.txt")

def log(username):
    with open(f'saves/{username}.txt', "r") as file:
        lines = file.readlines()

        infos = []
        
        for info in lines:
            infos.append(info)

    player = P.Player(int(infos[1]), int(infos[2]), int(infos[3]), infos[0])

    P.Player.setDifficulty(player, int(infos[4]))

    return player, int(infos[5]), int(infos[6])

def showProfile(player):
    print(f"\nProfil de {P.Player.getName(player)} :")
    print("————————————————————————————————————————————————")
    print(f"• Vie : {P.Player.getLP(player)}")
    print(f"• Force : {P.Player.getStrength(player)}")
    print(f"• Argent : {P.Player.getMoney(player)}€\n")
    print("————————————————————————————————————————————————")

def showMenu(mode):
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

    print("Voir la carte, tapez 'carte'")
    print("————————————————————————————————————————————————")
    print("Voir votre profil, tapez 'profil'")
    print("————————————————————————————————————————————————")

    if mode == "beggining":
        print("Voir ce qui vous attends, tapez 'événements'")
        print("————————————————————————————————————————————————")
        print("Définir le niveau de diffuculté, tapez 'difficulté'")
        print("————————————————————————————————————————————————")

    print("Commencer le jeu, tapez 'start'")
    print("\n≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠")

initGame()