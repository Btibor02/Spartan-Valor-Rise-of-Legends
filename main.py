import sys, time
import equipment
from getkey import getkey

INVENTORY = [equipment.Weapons.Kolós(), equipment.Shields.AspisOfHoplon(), equipment.Potions.Heal(), equipment.Potions.Shield()]

def printSlow(str):
    for l in str:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.02)


def gettingStarted():
    None


def startingDialog():
    printSlow("First let's take a look at your inventory: \n")
    keepInventory = True
    while keepInventory == True:
        print(f'Weapon = {INVENTORY[0][0]}')
        print(f'Shield = {INVENTORY[1][0]}')
        print(f'Equipment = {INVENTORY[2][3]}x {INVENTORY[2][0]}, {INVENTORY[3][3]}x {INVENTORY[3][0]},')
        keepInventory = False

    print("Would you like to take a look at the stats of an item? (y/n)")
    
    key = getkey()
    if key == "y":
        keepLookAtItems = True
        while keepLookAtItems == True:
            print(f'\n{"":-^147}\n')
            print("Choose an item: ")
            print("1. Weapon")
            print("2. Shield")
            print("3. Equipment")
            print("4. Close inventory")
            print(f'\n{"":-^147}\n')

            key = getkey()
            keepLookAtItems = False
            if key == "1":
                print(f'Name: {INVENTORY[0][0]}')
                print(f'{INVENTORY[0][1]}')
                print(f'Damage: {INVENTORY[0][2]}')
                print(f'Durability: {INVENTORY[0][3]}')
                print(f'Description: {INVENTORY[0][4]}')
                keepLookAtItems = True
            if key == "2":
                print(f'Name: {INVENTORY[1][0]}')
                print(f'{INVENTORY[1][1]}')
                print(f'Shield: {INVENTORY[1][2]}')
                print(f'Durability: {INVENTORY[1][3]}')
                print(f'Description: {INVENTORY[1][4]}')
                keepLookAtItems = True
            if key == "3":
                print("Choose an equipment: ")
                if INVENTORY[2][3] > 0:
                    print("1. Heal potion")
                elif INVENTORY[3][3] > 0:
                    print("2. Shield potion")
                    # ! Ha nincs heal akkor ez legyen az első
                # ! ha van kulcs akkor jelenjen meg
                else:
                    print("You do not have any equipment!")
                
                key = getkey()
                # TODO Ne lehessen megnyitni ha nincs neki
                if key == "1":
                    print(f'Name: {INVENTORY[2][0]}')
                    print(f'{INVENTORY[2][1]}')
                    print(f'Quantity: {INVENTORY[2][3]}')
                    print(f'Description: {INVENTORY[2][4]}')
                    
                if key == "2":
                    print(f'Name: {INVENTORY[3][0]}')
                    print(f'{INVENTORY[3][1]}')
                    print(f'Quantity: {INVENTORY[3][3]}')
                    print(f'Description: {INVENTORY[3][4]}')
                keepLookAtItems = True
            if key == "4":
                keepLookAtItems = False

    elif key == "n":
        keepInventory = False
        gettingStarted()



def intro():
    print("Would you like to see the intro? (y/n) ")
    key = getkey()
    if key == "y":
        printSlow("\nIn the golden era of Ancient Greece, when gods and mortals walked the earth together, you find yourself amidst the majestic city-states, where myths and legends come to life.\n"
                "The air is thick with the scent of olive groves and the distant echoes of pantheons. Yet, beneath the divine splendor and scholarly wisdom lies a realm teeming with untold mysteries.")
        printSlow("\nYou, a daring young adventurer, have been chosen by the fates to embark on a heroic quest that will unravel the secrets of Olympus itself.\n" 
                "The gods, in their eternal wisdom, have sensed an impending darkness creeping over the land. Ancient prophecies speak of a chosen one who would rise to challenge the shadows and restore balance to the mortal realm.")
        printSlow("\nAs you set forth on this odyssey, you will uncover forgotten relics, decipher cryptic scrolls, and forge alliances with legendary heroes.\n" 
                "The echoes of your adventures will resound through the ages, leaving an indelible mark on the annals of Greek mythology.")
        printSlow("\nYour decisions will shape the fate of not just your own destiny, but the destiny of all Greece.")
        printSlow("\nPrepare to step into the sandals of a hero, for the fate of an entire civilization rests upon your shoulders.\n" 
                "The gods are watching, mortal, and Olympus trembles in anticipation. Will you rise to the challenge and become the stuff of legends?")
        printSlow("\nThe epic adventure of a lifetime awaits in the land where gods and heroes collide. Your journey begins now.\n")
        print(f'\n{"":-^147}\n')

        startingDialog()
    elif key == "n":
        startingDialog()
        


def newGame():
    name = input("Please enter your character's name: ")
    print(f'Hello {name}! Are you ready to start your journey?')
    print("1. Yes")
    print("2. No")
    print(f'\n{"":-^147}\n')

    key = getkey()

    if key == "1":
        intro()
    elif key == "2":
        mainMenu()



def loadGame():
    None
    # ! Will be later implemented

def mainMenu():
    keepMenu = True
    while keepMenu == True:
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
        

        key = getkey()
        print(f'\n{"":-^147}\n')

        if key == "1":
            keepMenu = False
            newGame()
        elif key == "2":
            keepMenu = False
            loadGame()
        elif key == "3":
            keepMenu = False
    
    
mainMenu()