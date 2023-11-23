import sys, time, random, os
import equipments, dialogues, enemies, items
from getkey import getkey

global PLAYERSTATS
global INVENTORY
global NAME
TEXTBRAKE = f'\n{"":-^147}\n'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED    = '\33[31m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printSlow(str):
    for l in str:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.02)


def playerAttack(enemy, weapon):
    healPotion = list(INVENTORY[2])
    if PLAYERSTATS[0] > 0:
        key = getkey()
        os.system('cls||clear')
        match key:
            case "1":
                chance = random.randint(0, 10)
                if chance >= 0 and chance <= 6:
                    dmg = INVENTORY[0][2]
                    print(f'You did {dmg} damage')
                    enemy[4] -= dmg
                    weapon[3] -= 1
                if chance > 6 and chance <= 9:
                    print(f'{enemy[0]} blocked your attack')
                    if INVENTORY[0][2] - enemy[3] <= 0:
                        print("Your weapon did not do any damage") 
                    else:
                        dmg = INVENTORY[0][2] - enemy[3]
                        print(f'You did {dmg} damage')
                        enemy[4] -= dmg
                        weapon[3] -= 1
                if chance == 10:
                    print(f'{enemy[0]} evaded your attack')
                    print("You did 0 damage")
                print(f'HP: {enemy[4]}')
            case "2":
                # TODO a shield potinak legyen értelme
                # ? Ha van shield, akkor onnan a dmg onnan vonódjon le, ezt majd akkor kell megcsinálni ha tudok tesztelni rendes ellenséggel
                if INVENTORY[2][3] == 0 and INVENTORY[3][3] == 0:
                    print("You do not have any equipment!")
                else:
                    counter = 1
                    for i in range(len(INVENTORY)-2):
                        if INVENTORY[i + 2][3] > 0:
                            print(f'{counter}. {INVENTORY[i + 2][0]}')
                            counter += 1            
                key = getkey()
                if key == "1" and INVENTORY[2][3] > 0:
                    if PLAYERSTATS[0] == 100:
                        print("You can not use a Heal potion because you have max hp\n")
                    else:
                        if PLAYERSTATS[0] > 80:
                            healed = 100 - PLAYERSTATS[0]
                            PLAYERSTATS[0] += healed
                            healPotion[3] -= 1
                            INVENTORY[2] = healPotion

                            print(f'You healed {healed} hp and reached max hp\n')
                        else:
                            print("You healed 20 hp")
                            PLAYERSTATS[0] += 20
                            healPotion[3] -= 1
                            INVENTORY[2] = healPotion
                            print(f'Your new hp: {PLAYERSTATS[0]}\n')
    else:
        print("You have died!\nWould you like to start again? (y/n)")
        key = getkey()
        match key:
            case "y":
                os.system('cls||clear')
                mainMenu()
            case "n":
                quit()
    print(TEXTBRAKE)

    return enemy, weapon


def enemyAttack(enemy, shield):
    chance = random.randint(0, 10)
    if chance >= 0 and chance <= 6:
        dmg = enemy[2]
        print(f'{enemy[0]} did {dmg} damage')
        PLAYERSTATS[0] -= dmg
    if chance > 6 and chance <= 9:
        print(f"You blocked {enemy[0]}'s attack")
        shield[3] -= 1
        if enemy[2] - INVENTORY[1][2] <= 0:
            print(f"{enemy[0]}'s weapon did not do any damage")
        else:
            dmg = enemy[2] - INVENTORY[1][2]
            print(f'{enemy[0]} did {dmg} damage')
            PLAYERSTATS[0] -= dmg
    if chance == 10:
        print(f"You evaded {enemy[0]}'s attack")
        print(f"{enemy[0]} did 0 damage")
    print(f'Your HP: {PLAYERSTATS[0]}')
    print(TEXTBRAKE)
        
    return enemy, shield



def fight(enemy):
    enemy = list(enemy)
    enemyStillAlive = True
    print(TEXTBRAKE)
    print(f'\nName: {enemy[0]}')
    print(f'{enemy[1]}\n')
    print(f'Damage: {enemy[2]}')
    print(f'Block: {enemy[3]}')
    print(f'HP: {enemy[4]}')
    print(TEXTBRAKE)

    weapon = list(INVENTORY[0])
    shield = list(INVENTORY[1])
    while enemyStillAlive:
        if enemy[4] <= 0:
            print(f'Congratulation! You have defeated {enemy[0]}!')
            INVENTORY[0] = weapon
            INVENTORY[1] = shield
            foundGold = random.randint(0,100)
            PLAYERSTATS[2] += foundGold
            healPotion = list(INVENTORY[2])
            foundHealPotion = random.randint(0,3)
            healPotion[3] += foundHealPotion
            print(f'You have found {foundGold} gold and {foundHealPotion} Heal Potions')
            INVENTORY[2] = healPotion
            enemyStillAlive = False
        else:
            if enemy[4] > 0:
                print("What would you like to do? ")
                print("1. Attack")
                print("2. Use equipment")
                print(TEXTBRAKE)
                playerAttack(enemy=enemy, weapon=weapon)
                if enemy[4] > 0:
                    enemyAttack(enemy=enemy, shield=shield)
        
    
    # TODO loot odadása
    
    return


def checkInventory():
    keepInventory = True
    print("INVENTORY")
    while keepInventory == True:
        print(f'Weapon = {INVENTORY[0][0]}')
        print(f'Shield = {INVENTORY[1][0]}')
        print(f'Gold = {PLAYERSTATS[2]}')
        equipment = ""
        for i in range(len(INVENTORY)-2):
            try:
                equipment += f'{INVENTORY[i + 2][3]}x {INVENTORY[i + 2][0], }, '
            except:
                equipment = equipment
        print(f'Equipment = {equipment}')
        keepInventory = False

    print("Would you like to take a look at the stats of an item? (y/n)")
    
    key = getkey()
    match key:
        case "y":
            keepLookAtItems = True
            while keepLookAtItems == True:
                print(TEXTBRAKE)
                print("Choose an item: ")
                print("1. Weapon")
                print("2. Shield")
                print("3. Equipment")
                print("4. Close inventory")
                print(TEXTBRAKE)

                key = getkey()
                keepLookAtItems = False
                match key:
                    case "1":
                        print(f'Name: {INVENTORY[0][0]}')
                        print(f'{INVENTORY[0][1]}')
                        print(f'Damage: {INVENTORY[0][2]}')
                        print(f'Durability: {INVENTORY[0][3]}')
                        print(f'Description: {INVENTORY[0][4]}')
                        keepLookAtItems = True
                    case "2":
                        print(f'Name: {INVENTORY[1][0]}')
                        print(f'{INVENTORY[1][1]}')
                        print(f'Shield: {INVENTORY[1][2]}')
                        print(f'Durability: {INVENTORY[1][3]}')
                        print(f'Description: {INVENTORY[1][4]}')
                        keepLookAtItems = True
                    case "3":
                        print("Choose an equipment: ")
                        if INVENTORY[2][3] == 0 and INVENTORY[3][3] == 0:
                            print("You do not have any equipment!")
                        else:
                            counter = 1
                            for i in range(len(INVENTORY)-2):
                                if INVENTORY[i + 2][3] > 0:
                                    print(f'{counter}. {INVENTORY[i + 2][0]}')
                                    counter += 1
                            key = getkey()
                            potion = 2
                            if counter == 2:
                                if INVENTORY[2][3] > 0:
                                    potion = 2
                                else:
                                    potion = 3

                            if key == "1":
                                print(f'Name: {INVENTORY[potion][0]}')
                                print(f'{INVENTORY[potion][1]}')
                                print(f'Quantity: {INVENTORY[potion][3]}')
                                print(f'Description: {INVENTORY[potion][4]}')
                            
                            elif key == "2" and counter == 3:
                                print(f'Name: {INVENTORY[counter][0]}')
                                print(f'{INVENTORY[counter][1]}')
                                print(f'Quantity: {INVENTORY[counter][3]}')
                                print(f'Description: {INVENTORY[counter][4]}')
                        # TODO ha van kulcs akkor jelenjen meg
                        keepLookAtItems = True
                    case "4":
                        keepLookAtItems = False

        case "n":
            keepInventory = False
            os.system('cls||clear')
    return


def buyItemsInShop(item, type):
    PLAYERSTATS[2] -= item[5]
    if type == "weapon":
        INVENTORY[0] = item
    elif type == "shield":
        INVENTORY[1] = item
    elif type == "other":
        if item[0] == "Heal potion":
            selectedPotion = list(INVENTORY[2])
            selectedPotion[3] += 1
            INVENTORY[2] = selectedPotion
        elif item[0] == "Shield potion":
            selectedPotion = list(INVENTORY[3])
            selectedPotion[3] += 1
            INVENTORY[3] = selectedPotion
            
    print(TEXTBRAKE)
    print(f'Congratulation! You bought {item[0]}.')
    print(f'New gold balance: {PLAYERSTATS[2]}')
    print(TEXTBRAKE)
    checkInventory()


def lookAtItemsInShop(item, type):
    colorDecider1 = bcolors.RED
    colorDecider2 = bcolors.RED
    if type == "weapon":
        if item[2] > INVENTORY[0][2]:
            colorDecider1 = bcolors.OKGREEN
        if item[3] > INVENTORY[0][3]:
            colorDecider2 = bcolors.OKGREEN

        print(f'Name: {item[0]}')
        print(f'{item[1]}')
        print('Damage: ' + colorDecider1 + str(item[2]) + bcolors.ENDC)
        print('Durability: ' + colorDecider2 + str(item[3]) + bcolors.ENDC)
        print(f'Description: {item[4]}')
        print(f'Price: {item[5]}')
        print(TEXTBRAKE)
    elif type == "shield":
        if item[2] > INVENTORY[1][2]:
            colorDecider1 = bcolors.OKGREEN
        if item[3] > INVENTORY[1][3]:
            colorDecider2 = bcolors.OKGREEN

        print(f'Name: {item[0]}')
        print(f'{item[1]}')
        print('Shield: ' + colorDecider1 + str(item[2]) + bcolors.ENDC)
        print('Durability: ' + colorDecider2 + str(item[3]) + bcolors.ENDC)
        print(f'Description: {item[4]}')
        print(f'Price: {item[5]}')
        print(TEXTBRAKE)
    elif type == "other":
        print(f'Name: {item[0]}')
        print(f'{item[1]}')
        print(f'Description: {item[4]}')
        print(f'Price: {item[5]}')
        print(TEXTBRAKE)

    print("Would you like to buy this item? (y/n)")
    key = getkey()
    match key:
        case "y":
            if PLAYERSTATS[2] < item[5]:
                goldDiff = item[5] - PLAYERSTATS[2]
                print(f'You do not have enough gold to buy this item. Missing: {goldDiff}')
                return
            else:
                buyItemsInShop(item=item, type=type)
        case "n":
            return
        



def hiddenPeddlerShop():
    # TODO Ha párszor össze vissza megy a user akkor többször kell kilépni, ezt kell megoldani
    keepBrowsing = True
    while keepBrowsing:
        print("HIDDEN PEDDLER")
        print("1. Weapons")
        print("2. Shields")
        print("3. Equipments")
        print("Q - Quit")
        print(TEXTBRAKE)

        key = getkey()
        match key:
            case "1":
                print("1. Xiphos")
                print("2. Labrys")
                print("B - Back")
                print(TEXTBRAKE)

                key = getkey()
                match key:
                    case "1" :
                        item = equipments.Weapons.Xiphos()
                        if INVENTORY[0] == item:
                            print("You already own this item!")
                            hiddenPeddlerShop()
                        else:
                            lookAtItemsInShop(item=item, type="weapon")
                    case "2" :
                        item = equipments.Weapons.Labrys()
                        if INVENTORY[0] == item:
                            print("You already own this item!")
                            hiddenPeddlerShop()
                        else:
                            lookAtItemsInShop(item=item, type="weapon")
                    case "b":
                        hiddenPeddlerShop()
            case "2":
                print("1. Pelte")
                print("2. Thureos")
                print("B - Back")
                print(TEXTBRAKE)

                key = getkey()
                match key:
                    case "1" :
                        item = equipments.Shields.Pelte()
                        if INVENTORY[1] == item:
                            print("You already own this item!")
                            print(TEXTBRAKE)
                            hiddenPeddlerShop()
                        else:
                            lookAtItemsInShop(item=item, type="shield")
                    case "2" :
                        item = equipments.Shields.Thureos()
                        print(INVENTORY[0], INVENTORY[0] == item, item)
                        if INVENTORY[1] == item:
                            print("You already own this item!")
                            print(TEXTBRAKE)
                            hiddenPeddlerShop()
                        else:
                            lookAtItemsInShop(item=item, type="shiled")
                    case "b":
                        hiddenPeddlerShop()
            case "3":
                print("1. Heal Potion")
                print("2. Shield Potion")
                print(TEXTBRAKE)
                key = getkey()
                match key:
                    # ? Max mennyiség?
                    # TODO egyszerre lehessen többet venni
                    case "1":
                        item = equipments.Potions.Heal()
                        lookAtItemsInShop(item=item, type="other")
                    case "2":
                        item = equipments.Potions.Shield()
                        lookAtItemsInShop(item=item, type="other")
                    # ? Több equipment?
            case "q":
                return


def hiddenPeddler():
    dialogues.Start.hiddenPeddler(chapter=1)

    key = getkey()
    match key:
        case "y":
                print(TEXTBRAKE)
                printSlow(bcolors.BOLD+ "Hidden Peddler: " + bcolors.ENDC + "Ah, a seeker of the arcane, I see. In these woods, secrets are my trade.\n"
                        "\tPotions brewed under the moon's watchful eye, herbs plucked from the oldest groves, and swords and shields, each bearing the essence of this ancient realm. What brings you to my humble emporium?")
                print(TEXTBRAKE)
                hiddenPeddlerShop()
                

        case "n":
                printSlow("\nYou continue your journey towards the cript.\n")
                # ! INNEN FOLYTATÓDIK
                quit
    


def parnassusForest():
    chance = random.randint(0, 10) 
    dialogues.Start.parnassusForest(chance=chance, first = True)
    PLAYERSTATS[2] += 50
    if chance >= 7:
        print(f'Name: {equipments.Weapons.Dory()[0]}')
        print(f'{equipments.Weapons.Dory()[1]}')
        print('Damage: ' + bcolors.OKGREEN + str(equipments.Weapons.Dory()[2]) + bcolors.ENDC)
        print('Durability: ' + bcolors.OKGREEN + str(equipments.Weapons.Dory()[3]) + bcolors.ENDC)
        print(f'Description: {equipments.Weapons.Dory()[4]}')
        print(TEXTBRAKE)

        print("Would you like to take it? (y/n)")
        key = getkey()
        match key:
            case"y":
                INVENTORY[0] = equipments.Weapons.Dory()
                TEXTBRAKE
                checkInventory()
            case"n":
                None
    dialogues.Start.parnassusForest(chance=chance, first=False)
    fight(enemy=enemies.Enemies.forestSentinel())
    hiddenPeddler()


def tutorialFight():
    printSlow("But before you go further, you see a mannequin, and since you haven't fought in a while, you decide to start practicing")
    printSlow("\nYou can see the opponent's statistics before every battle, and you can take various actions")

    fight(enemy=enemies.Enemies.mannequin())
    parnassusForest()




def startingDialog():
    printSlow("First let's take a look at your inventory: \n")
    checkInventory()
    print("Would you like to skip the dialogue? (y/n) ")
    key = getkey()
    match key:
        case "n":
            dialogues.Start.thalassa()
            print(TEXTBRAKE)
            tutorialFight()
        case "y":
            tutorialFight()
    



def intro():
    print("Would you like to skip the intro? (y/n) ")
    key = getkey()
    match key:
        case "n":
            dialogues.Start.intro()
            print(TEXTBRAKE)
            startingDialog()
        case "y":
            startingDialog()
        


def newGame():
    NAME = input("Please enter your character's name: ")
    print(f'Hello {NAME}! Are you ready to start your journey?')
    print("1. Yes")
    print("2. No")
    print(TEXTBRAKE)

    key = getkey()
    match key:
        case "1":
            os.system('cls||clear')
            intro()
        case "2":
            mainMenu()



def loadGame():
    None
    # TODO Will be later implemented
    # TODO font size should be changeable

def mainMenu():
    keepMenu = True
    while keepMenu == True:
        os.system('cls||clear')
        print(""" 
             _____                  _                _   _       _             ______ _                   __   _                               _     
            /  ___|                | |              | | | |     | |            | ___ (_)                 / _| | |                             | |    
            \ `--. _ __   __ _ _ __| |_ __ _ _ __   | | | | __ _| | ___  _ __  | |_/ /_ ___  ___    ___ | |_  | |     ___  __ _  ___ _ __   __| |___ 
             `--. \ '_ \ / _` | '__| __/ _` | '_ \  | | | |/ _` | |/ _ \| '__| |    /| / __|/ _ \  / _ \|  _| | |    / _ \/ _` |/ _ \ '_ \ / _` / __|
            /\__/ / |_) | (_| | |  | || (_| | | | | \ \_/ / (_| | | (_) | |    | |\ \| \__ \  __/ | (_) | |   | |___|  __/ (_| |  __/ | | | (_| \__ \ 
            \____/| .__/ \__,_|_|   \__\__,_|_| |_|  \___/ \__,_|_|\___/|_|    \_| \_|_|___/\___|  \___/|_|   \_____/\___|\__, |\___|_| |_|\__,_|___/
                | |                                                                                                      __/ |                     
                |_|                                                                                                     |___/                      
            """)
        print(f'{"Main menu":.^146}')
        print(f'\n{"1. New Game":^146}')
        print(f'{"2. Load Game":^146}')
        # ? Később akár settings és difficulty választás
        print(f'{"3. Exit":^141}')

        global PLAYERSTATS
        global INVENTORY
        global NAME

        PLAYERSTATS = [100, 0, 1000] #HP, SHIELD, GOLD
        # ! VISSZAVÁLTOZTATNI A GOLDOT 100-RA
        INVENTORY = [equipments.Weapons.Kolós(), equipments.Shields.AspisOfHoplon(), equipments.Potions.Heal(), equipments.Potions.Shield()]
        NAME = ""

        key = getkey()
        print(TEXTBRAKE)
        match key:
            case "1":
                keepMenu = False
                newGame()
            case "2":
                keepMenu = False
                loadGame()
            case "3":
                keepMenu = False
            case "4":
                # ! TESZT mód
                keepMenu = False
                hiddenPeddler()
    
    
mainMenu()