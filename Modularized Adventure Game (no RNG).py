
class Hero:
    def __init__(self, name, armor, sword, shield):
        self.name = name
        self.armor = armor 
        self.sword = sword
        self.shield = shield

    def set_name(self,name):
        self.name = name 

    def equip_armor(self,armor_type):
        self.armor = armor_type 

    def equip_sword(self, sword_type):
        self.sword = sword_type

    def equip_shield(self, shield_type):
        self.shield = shield_type

hero = Hero(name= None, armor = None, sword = None, shield = None)

def run():
    while True:
        answer = input("Do you want to play a game? (yes/no)").lower().strip()

        if answer == "yes":
            answer = input("What is your name?")
            hero.name = answer
            print("\n \n \n \n" + "Welcome to the beginning of your Adventure \n Hero-" + hero.name)
            answer = input ("You open your eyes and see a fork in the road, \n do you want to travel east or west?").lower().strip()
            if answer == "east":
                Epath()
            
            elif answer == "west":
                Wpath()

def Wpath():
    answer = input("\n \n \n \n" + hero.name + " encounter a large ogre, \n do you want to run or attack?").lower().strip()
    if answer == "attack":
        print("Poor choice, with no weapon in hand the orge ends your adventure almost instantaneously!\n Is that really the best you can do?")

    elif answer == "run":
        Epath()
    
def Epath():
    print("\n \n \n \n" + hero.name + " reaches a forest with territorial markings on your north side.")
    answer = input ("Do you continue east or go north? \n (Answer with east or north)").lower().strip()
    if answer == "north":
        ENpath()
    
    elif answer == "east":
        EEpath()

def ENpath():
    answer = input("\n \n \n \n" + hero.name + " enters the bears territory accidently. \n Mother bear approaches you slowly.\n (Retreat or fight)").lower().strip()
    if answer == "fight":
        print("A mother bear ambushes you for tresspassing into her territory, \n your journey has ended")
    
    elif answer == "retreat":
        Epath()

def EEpath():
    answer = input("\n \n \n \n" + hero.name + " feel faint hunger as you walk into a colony of rabbits,\n do you hunt the rabbits or continue your journey?\n (answer with hunt or continue)").lower().strip()
    if answer == "continue":
        print(hero.name + "You pass out from fatigue never to awake again. \n Game Over.")

    if answer == "hunt":
        print("\n \n \n \n" + "Your hunger has been satisfied and extra food is stored in your satchel. \n You continue your journey eastward until you come across a few different items.")
        answer = input ("Do you take the sword, shield or armor?\n (Being greedy might not mean your downfall here)").lower().strip()
        
        if answer == "sword":
            SwordPath()
        
        elif answer == "shield":
            ShieldPath()
        
        elif answer == "armor":
            ArmorPath()

        elif answer == "all":
            SecretPath()

def SwordPath():
    print("\n \n \n \n" + "You feel empowered by the spirit of the sword's previous weilder + 3000% damage")
    hero.sword = "Sword of the Savior"
    print("You have equiped the Sword of the Savior")
    answer = input("Which direction do you travel? east or north?").lower().strip()
    if answer == "east":
        EONEWpPath()
        
    elif answer == "north":
        NONEWpPath()

def ShieldPath():
    print("\n \n \n \n" + "Your shield feels impenetrable and you feel as if you can block anything -99% hit chance to all enemies + 5000 defense points")
    hero.shield = "Havoc's Shield"
    print("You have equipped Havoc's Shield")
    answer = input("Which direction do you travel? East or north?").lower().strip()
    if answer == "east":
        EONEWpPath()

    elif answer == "north":
        NONEWpPath()

def ArmorPath():
    print("\n \n \n \n" + "You feel as if you are unmoveable and sturdier than ever + 10000 defense points, bare-handed attacks incapacitate enemies")
    hero.armor = "Golden armor"
    print("You have equipped the Legendary Golden Armor")
    answer = input("Which direction do you travel? East or north?").lower().strip()
    if answer == "east":
        EONEWpPath()

    elif answer == "north":
        NONEWpPath()

def EONEWpPath():
    print("\n \n \n \n" + "You reach a cliff, trees are covering the ground below.")
    answer = input ("Travel to the tower in the distance or see whats at the bottom of the cliff? \n(answer tower or cliff.)").lower().strip()
    if answer == "cliff":
        print("You foolishly jump off the cliff, \n you not only break your legs but end up surrounded by orcs. \nGame Over.")

    if answer == "tower":
        ONEFTowerPath()

def NONEWpPath():
    answer = input ("\n \n \n \n" + "You enter the bears territory accidently. \n Mother bear approaches you slowly. \n (Retreat or fight)").lower().strip()
    if answer == "retreat":
        EONEWpPath()
    
    if answer == "fight":
        print("\n \n \n \n" + hero.name + " incapacitates the bear easily, but it feeks though there is another presence and glance at your equipment for a moment.")
        EONEWpPath()

def ONEFTowerPath():
    print("\n \n \n \n" + hero.name + "  reaches the front gates of the tower.")
    answer = input("As you begin your descent in the tower you feel the bloodlust from the orcs below. \n Two enemies attempt to ambush you from above! \n (Counter or defend)")
    if answer == "defend":
        print("As you brace yourself you equipment speaks to you \n 'This world is not for those who wait to be struck' \n" + hero.name + "'s movements are restricted unable to stop the ambush. \n Game Over.")
    
    if answer == "counter":
        TWOFTowerPath()

def TWOFTowerPath():
    print("\n \n \n \n" + "Before the enemies can land " + hero.name + " casually dispatches the enemies")
    print(hero.name + " begins to get the feeling theres more to the equipment than the massive stats.")
    answer = input(hero.name + " walks into a room and prepares for combat with 3 orcs. \n Suddenly two more orcs attempt to attack you offguard from behind. \n How do you respond? (Strike or parry)")
    if answer == "parry":
        print("Your equipment speaks to your hesitant actions, cowardice is not accepted in this world. \n Your equipment shatters, unable to defend yourself \n" + hero.name + "s adventure ends")
    
    elif answer == "strike":
        THREEFTowerPath()

def THREEFTowerPath():
    print ("\n \n \n \n" + hero.name + " effortlessly defends themselves aggainst the surprise attack. \n Moments later" + hero.name + "incapacitates the three original enemies in the room")
    print(hero.name + " enters a room full of orcs, \n orcs of varying sizes with various weapons. \n The orcs stand aside as the leader prepares to engage 1 on 1 combat with you.")
    answer = input(hero.name + " have a brief opening before the leader rushes you. (Surprise or Wait)").lower().strip()
    if answer == "wait":
        print("Once the leader is finished preparing he lets out a loud roar and all of the orcs attack you at once. Game Over")
    
    elif answer == "surprise":
        print("\n \n \n \n" + "As you prepare to attack the orc leader, your equipment speaks to you")
        print(hero.name)
        print("You have completed the secret quest 'Courage of the Inexperienced'")
        print(" Skill [Moonlight Slash] Acquired")
        GameWinPath()

def GameWinPath():
    answer = input("Would you like to use [Moonlight Slash]? (Yes or no)")
    if answer == "no":
        print ("\n \n \n \n" + "Foolish Mortal you deserve nothing but death, \n Now perish \n The leader orc lets out a loud roar and all of the orcs attack you at once. \n Game Over.")

    elif answer == "yes":
        print ("\n \n \n \n" + "As " + hero.name + " finishes their attack it feels as though the bloodlust in the air has been cut.")
        print ("To the hero's surprise all of the orcs in the room begin bowing.")
        print ("The orc leader's body falls as a clean crescent shaped cut was made.")
        print ("The other orcs no longer have any intention to fight you.")
        print ("One orc proceeds to step forward and explain how the leader subjagated them")
        print ("The orcs proclaim you to be their new leader.")
        WinPath()

def WinPath():
    print ("\n \n \n \n" + "You have successfully completed the expedition. \n Congrations " + hero.name)
    answer = input ("Would you like to end the game? (Enter yes to end)")
    if answer == "yes":
        quit()

    else:
        quit()

def SecretPath():
    print("Immesurable power flows through you \n + 3000% damage, -99% enemy hit chance, \n 10000 defense points + set passive effect active 200% hp regen per second \n + 250% movespeed & -99.9% damage taken")
    hero.sword = "Sword of the Savior"
    hero.shield = "Havoc's Shield"
    hero.armor = "Golden armor"
    print(hero.name + " has equipped the following items, The Sword of the Savior, Havoc's Shield and Golden Armor")
    TowerfallPath()

def TowerfallPath():
    print("The set of equipment guides to a cliff eastward of where you were before.")
    print(hero.name + " looks over the cliff to see a hole, (about the size you can make it through) near the bottom.")
    print("The hero gets the inexplicable feeling that they'd be okay falling from this height.")
    print(hero.name + " jumps to and through the hole")
    print(hero.name + " enters the with room with such a fierce crash \n that an explosiive shockwaves sends most of the smaller enemies in the room flying into walls and others")
    print(hero.name + " shrugs the fall off as if it were nothing")
    print("What seems to be the boss orc begins to rush you. \n Time seems to have frozen, your armor speaks to you \n 'Fear not mortal, no worldly threat will harm you with this equipment on.' \n You have learned 2 new skills \n [Lacerate aquired] \n[Teleport acquired]")
    answer = input("Use skill Lacerate? (Yes or no)").lower().strip()
    if answer == "no":
        print("\n \n \n \n" + "A grim reaper like figure appears behind you with a scythe at your neck. \n It says 'It is a waste to be given such power and not use it', the reaper decapitates you. \n Game over.")
    
    if answer == "yes":
        print("\n \n \n \n" + "You swing your sword in a manner that carries you around the room not wildly but as if you were dancing. \n By the time you stop moving time feels as if it is moving again \n but none of the orcs are moving. \n As you sheathe your weapon, orcs drop in all directions,\n some decapitated others cleanly chopped in two at the waist.")
        print("The orc leader falls last but shakes the room when it does. \n You notice that not only did you defeat all of the enemies in the room but \n you cut the entire base of the tower.")
        answer = input("The entire tower is beginning to collapse and it seems you have no way out. \n [Use skill teleport?] (yes or no)")
        if answer == "no":
            print("Many floors of rubble proceed to fall on you. \n You are not killed but the rubble but you are unable to move. \n The equipment speaks to you 'Our new rest place has been decided.' \n You are stuck under rubble unable to move regretting not teleporting until you die due to famine. \n Game over.")

        elif answer =="yes":
            TowerDestructionPath()

def TowerDestructionPath():
    print("\n \n \n \n" + "You are teleported to the point where you jumped off the cliff.\n You smile know you can level entire buildings with ease and escape safely.\n You win " + hero.name + ".")
    answer = input ("Would you like to end the game? (Enter yes to end)")
    if answer == "yes":
        quit()

    else:
        quit()
            
run()