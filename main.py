import sys, time, random
import equipment, dialogues, enemies
from getkey import getkey

PLAYERSTATS = [100, 0] #HP, SHIELD
INVENTORY = [equipment.Weapons.Kolós(), equipment.Shields.AspisOfHoplon(), equipment.Potions.Heal(), equipment.Potions.Shield()]
NAME = ""
TEXTBRAKE = f'\n{"":-^147}\n'

def printSlow(str):
    for l in str:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.02)


def playerAttack(enemy):
    if PLAYERSTATS[0] > 0:
        key = getkey()
        if key == "1":
            chance = random.randint(0, 10)
            if chance >= 0 and chance <= 6:
                dmg = INVENTORY[0][2]
                print(f'You did {dmg} damage')
                enemy[4] -= dmg
            if chance > 6 and chance <= 9:
                print(f'{enemy[0]} blocked your attack')
                if INVENTORY[0][2] - enemy[3] <= 0:
                    print("Your weapon did not do any damage") 
                else:
                    dmg = INVENTORY[0][2] - enemy[3]
                    print(f'You did {dmg} damage')
                    enemy[4] -= dmg
            if chance == 10:
                print(f'{enemy[0]} evaded your attack')
                print("You did 0 damage")
            print(f'HP: {enemy[4]}')
            # TODO durability
        elif key == "2":
            # TODO a shieldnek potinak1 legyen értelme
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
                        print(f'You healed {healed} hp and reached max hp\n')
                    else:
                        print("You healed 20 hp")
                        PLAYERSTATS[0] += 20
                        print(f'Your new hp: {PLAYERSTATS[0]}\n')
            fight(enemy=enemy)
    else:
        print("You have died!\nWould you like to start again? (y/n)")
        key = getkey()
        if key == "y":
            mainMenu()
            # TODO minden statot visszaállitani az eredetire 
        elif key == "n":
            None
    print(TEXTBRAKE)

    return enemy


def enemyAttack(enemy):
    chance = random.randint(0, 10)
    if chance >= 0 and chance <= 6:
        dmg = enemy[2]
        print(f'{enemy[0]} did {dmg} damage')
        PLAYERSTATS[0] -= dmg
    if chance > 6 and chance <= 9:
        print(f"You blocked {enemy[0]}'s attack")
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
        
    return enemy



def fight(enemy):
    enemy = list(enemy)
    while enemy[4] > 0:
        print("What would you like to do? ")
        print("1. Attack")
        print("2. Use equipment")
        print(TEXTBRAKE)

        playerAttack(enemy=enemy)
        if enemy[4] > 0:
            enemyAttack(enemy=enemy)
        else:
            print(f'Congratulation! You have killed {enemy[0]}!')
            # TODO loot odadása
    
    # ! jutalmak elosztása
        
        

                



def checkInventory():
    keepInventory = True
    while keepInventory == True:
        print(f'Weapon = {INVENTORY[0][0]}')
        print(f'Shield = {INVENTORY[1][0]}')
        equipment = ""
        for i in range(len(INVENTORY)-2):
            try:
                equipment += f'{INVENTORY[i + 2][3]}x {INVENTORY[i + 2][0]}, '
            except:
                equipment = equipment
        print(f'Equipment = {equipment}')
        keepInventory = False

    print("Would you like to take a look at the stats of an item? (y/n)")
    
    key = getkey()
    if key == "y":
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
            if key == "4":
                keepLookAtItems = False

    elif key == "n":
        keepInventory = False
    return


def parnassusForest():
    None


def tutorialFight():
    printSlow("But before you go further, you see a mannequin, and since you haven't fought in a while, you decide to start practicing")
    printSlow("\nYou can see the opponent's statistics before every battle, and you can take various actions")
    print(TEXTBRAKE)
    print(f'\nName: {enemies.Enemies.mannequin()[0]}')
    print(f'{enemies.Enemies.mannequin()[1]}\n')
    print(f'Damage: {enemies.Enemies.mannequin()[2]}')
    print(f'Block: {enemies.Enemies.mannequin()[3]}')
    print(f'HP: {enemies.Enemies.mannequin()[4]}')
    print(TEXTBRAKE)

    fight(enemy=enemies.Enemies.mannequin())




def startingDialog():
    printSlow("First let's take a look at your inventory: \n")
    checkInventory()
    print("Would you like to skip the dialogue? (y/n) ")
    key = getkey()
    if key == "n":
        dialogues.Start.thalassa()
        print(TEXTBRAKE)
        tutorialFight()
    elif key == "y":
        tutorialFight()
    



def intro():
    print("Would you like to skip the intro? (y/n) ")
    key = getkey()
    if key == "n":
        dialogues.Start.intro()
        print(TEXTBRAKE)
        startingDialog()
    elif key == "y":
        startingDialog()
        


def newGame():
    NAME = input("Please enter your character's name: ")
    print(f'Hello {NAME}! Are you ready to start your journey?')
    print("1. Yes")
    print("2. No")
    print(TEXTBRAKE)

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
        print(TEXTBRAKE)

        if key == "1":
            keepMenu = False
            newGame()
        elif key == "2":
            keepMenu = False
            loadGame()
        elif key == "3":
            keepMenu = False
    
    
mainMenu()