import random
import time


def radn(input):
    i = input + random.randint(0, input)
    i * input + random.randint(0, i)
    i / input
    if i < input:
        i += i
    if i > input * 5:
        i -= i + input

    return i


def miss(low, high):
    i = random.randint(low, high)

    if i > 1:
        i = 1
    elif i < 1:
        i = 0
    return i


def combat(playerH, playerA, enemyN, enemyH, enemyA, roomToBeDone, amountofenemies):
    print("You will kill this " + str(enemyN) + "...")
    while enemyH >= 0:
        if miss(-20, 15) == 1:
            print("The " + str(enemyN) + " attacked you before you could it...")
            if miss(-20, 20) == 1:
                time.sleep(1.5)
                playerH = playerH - enemyA
                if playerH <= 0:
                    print("The " + str(enemyN) + " killed you...")
                    time.sleep(1)
                    exit(0)
                else:
                    print("The " + str(enemyN) + " attacked you and you have " + str(playerH) + " HP left...")
            else:
                print("The " + str(enemyN) + " missed!")
        else:
            time.sleep(1.3)
            print("You attack the " + str(enemyN) + "...")
            if miss(-20, 30) == 1:
                enemyH = enemyH - playerA
                time.sleep(1.5)
                if enemyH <= 0:
                    print(" ")
                    print("You killed the " + str(enemyN) + "...")
                    time.sleep(1)
                    print("""
                        
                        
                        
                        
                        
                    """)
                    time.sleep(1)
                    amountofenemies -= 1
                    roomToBeDone = True
                else:
                    print("You attacked the " + str(enemyN) + " and it has " + str(enemyH) + " HP left...")
            else:
                print("You missed!")
    return roomToBeDone


class Room:
    def __init__(self):
        self.rHealth = radn(10)
        self.rAttack = radn(2)
        self.aHealth = radn(15)
        self.aAttack = radn(4)
        self.pHealth = radn(20)
        self.pAttack = radn(5)
        self.ratsInB = random.randint(1, 3)
        self.ratsInC = random.randint(1, 3)
        self.ratsInD = random.randint(1, 3)
        self.adone = False
        self.bdone = False
        self.cdone = False
        self.ddone = False
        self.lockeddone = False
        self.hasKey = False
        self.hasGrain = False

    def a(self):
        if self.adone:
            self.anorat()
        else:
            print("""
                You slowly pull open the creaking wooden door. Dust falls to your feet as it swings open, revealing
                knotty wooden steps leading down into a thick darkness.
            """)
            time.sleep(4)
            print("""
                You walk down the steps, which bend under your weight, into the darkness, until you step firmly
                onto an earthen floor. As your eyes begin to adjust to the absence of light, you hear a swift rustling
                noise and see a quick flash of glistening teeth as a huge RAT leaps upon you!
            """)
            time.sleep(7)
            print(""" It's fightin' time!
    
                [1] Run
                [2] Flee
                [3] Get away!
                [4] Fight!
                [5] EEEEEEK!
                [6] Wait...
            """)

            try:
                r1Num = int(input("Your response: "))
            except ValueError:
                print("Your response can not be a string; try a number.")
                r1Num = input("Your response: ")

            if int(r1Num) > 6 or int(r1Num) < 1:
                print("Your response can not be more than 6 or less than 0")
                try:
                    r1Num = int(input("Your response: "))
                except ValueError:
                    print("Your response can not be a string; try a number.")
                    r1Num = input("Your response: ")

            if r1Num == 6:
                print("The traveler stands and waits for the rat to take his life...")
                time.sleep(3)
                print("""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                """)
                print("Wow. I didn't think anyone was dumb enough to pick that. Enjoy your Fate...")
                time.sleep(1)
                exit(0)
            elif r1Num == 4:
                if combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.adone, 1):
                    self.adone = True

                print("""
                
                
                text here
                
                
                
                
                
                [1] Look around the room.
                [2] Go to the next room.
                
                
                """)

                try:
                    r1Num2 = int(input("Your response: "))
                except ValueError:
                    print("Your response can not be a string; try a number.")
                    r1Num2 = input("Your response: ")

                if int(r1Num2) > 2 or int(r1Num2) < 1:
                    print("Your response can not be more than 2 or less than 0")
                    try:
                        r1Num2 = int(input("Your response: "))
                    except ValueError:
                        print("Your response can not be a string; try a number.")
                        r1Num2 = input("Your response: ")

                if r1Num2 == 1:
                    print("""
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    The room has nothing in it but a locked door, a hallway to the next room, and a hole in the wall.
                    """)
                    time.sleep(2)

                    print("""
    
    
                    text here
    
    
    
    
    
                    [2] Go to the next room.
    
    
                    """)

                    try:
                        r1Num2 = int(input("Your response: "))
                    except ValueError:
                        print("Your response can not be a string; try a number.")
                        r1Num2 = input("Your response: ")

                    if int(r1Num2) > 2 or int(r1Num2) < 1:
                        print("Your response can not be more than 2 or less than 0")
                        try:
                            r1Num2 = int(input("Your response: "))
                        except ValueError:
                            print("Your response can not be a string; try a number.")
                            r1Num2 = input("Your response: ")
                    if r1Num2 == 2:
                        self.b()
                elif r1Num2 == 2:
                    self.b()

            else:
                exit(0)

    def b(self):
        if self.bdone:
            self.bnorat()
        else:
            print("There are " + str(self.ratsInB) + "rats...")
            print(""" It's fightin' time!

                            [1] Run
                            [2] Fight!
                        """)

            try:
                r2Num = int(input("Your response: "))
            except ValueError:
                print("Your response can not be a string; try a number.")
                r2Num = input("Your response: ")

            if int(r2Num) > 2 or int(r2Num) < 1:
                print("Your response can not be more than 2 or less than 0")
                try:
                    r2Num = int(input("Your response: "))
                except ValueError:
                    print("Your response can not be a string; try a number.")
                    r2Num = input("Your response: ")

            if r2Num == 1:
                print("The traveler tries to run back a room...")
                if miss(-20, 20):
                    print("The traveler succeeds!")
                    self.anorat()
                else:
                    print("The traveler could not get away...")
                    if self.ratsInB == 1:
                        if combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.bdone,
                                  self.ratsInB):
                            self.bdone = True
                    elif self.ratsInB == 2:
                        if combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.bdone,
                                  self.ratsInB) and combat(self.pHealth, self.pAttack, "rat", self.rHealth,
                                                           self.rAttack, self.bdone, self.ratsInB):
                            self.bdone = True
                    elif self.ratsInB == 3:
                        if combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.bdone,
                                  self.ratsInB) and combat(self.pHealth, self.pAttack, "rat", self.rHealth,
                                                           self.rAttack, self.bdone, self.ratsInB) and combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.bdone, self.ratsInB):
                            self.bdone = True
            elif r2Num == 2:
                if self.ratsInB == 1:
                    if combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.bdone, self.ratsInB):
                        self.bdone = True
                elif self.ratsInB == 2:
                    if combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.bdone,
                              self.ratsInB) and combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack,
                                                       self.bdone, self.ratsInB):
                        self.bdone = True
                elif self.ratsInB == 3:
                    if combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.bdone,
                              self.ratsInB) and combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack,
                                                       self.bdone, self.ratsInB) and combat(self.pHealth, self.pAttack,
                                                                                            "rat", self.rHealth,
                                                                                            self.rAttack, self.bdone,
                                                                                            self.ratsInB):
                        self.bdone = True
                print("""


                                   text here





                                   [1] Look around the room.
                                   [2] Go to the next room.
                                   [3] Go back a room.


                                   """)

                try:
                    r2Num2 = int(input("Your response: "))
                except ValueError:
                    print("Your response can not be a string; try a number.")
                    r2Num2 = input("Your response: ")

                if int(r2Num2) > 3 or int(r2Num2) < 1:
                    print("Your response can not be more than 3 or less than 0")
                    try:
                        r2Num2 = int(input("Your response: "))
                    except ValueError:
                        print("Your response can not be a string; try a number.")
                        r2Num2 = input("Your response: ")

                if r2Num2 == 1:
                    print("""













                                       desc of room
                                       """)
                    time.sleep(2)

                    print("""


                                       text here





                                       [2] Go to the next room.
                                       [3] Go back a room.


                                       """)

                    try:
                        r2Num2 = int(input("Your response: "))
                    except ValueError:
                        print("Your response can not be a string; try a number.")
                        r2Num2 = input("Your response: ")

                    if int(r2Num2) > 3 or int(r2Num2) < 1:
                        print("Your response can not be more than 3 or less than 0")
                        try:
                            r2Num2 = int(input("Your response: "))
                        except ValueError:
                            print("Your response can not be a string; try a number.")
                            r2Num2 = input("Your response: ")
                    if r2Num2 == 2:
                        self.c()
                    elif r2Num2 == 3:
                        self.a()
                elif r2Num2 == 2:
                    self.c()
                elif r2Num2 == 3:
                    self.a()

    def c(self):
        if self.cdone:
            self.cnorat()
        else:
            print("There are " + str(self.ratsInC) + "rats...")
            print("""  
            
            
            
                It's fightin' time!

                        [1] Run
                        [2] Fight!
                                    """)

            try:
                r3Num = int(input("Your response: "))
            except ValueError:
                print("Your response can not be a string; try a number.")
                r3Num = input("Your response: ")

            if int(r3Num) > 2 or int(r3Num) < 1:
                print("Your response can not be more than 2 or less than 0")
                try:
                    r3Num = int(input("Your response: "))
                except ValueError:
                    print("Your response can not be a string; try a number.")
                    r3Num = input("Your response: ")

            if r3Num == 1:
                print("The traveler tries to run back a room...")
                if miss(-20, 20):
                    print("The traveler succeeds!")
                    self.bnorat()
                else:
                    if self.ratsInC == 1:
                        if combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.cdone,
                                  self.ratsInC):
                            self.cdone = True
                    elif self.ratsInB == 2:
                        if combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.cdone,
                                  self.ratsInC) and combat(self.pHealth, self.pAttack, "rat", self.rHealth,
                                                           self.rAttack,
                                                           self.cdone, self.ratsInC):
                            self.cdone = True
                    elif self.ratsInC == 3:
                        if combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.cdone,
                                  self.ratsInC) and combat(self.pHealth, self.pAttack, "rat", self.rHealth,
                                                           self.rAttack,
                                                           self.cdone, self.ratsInC) and combat(self.pHealth,
                                                                                                self.pAttack,
                                                                                                "rat", self.rHealth,
                                                                                                self.rAttack,
                                                                                                self.cdone,
                                                                                                self.ratsInC):
                            self.cdone = True
            elif r3Num == 2:
                if self.ratsInC == 1:
                    if combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.cdone, self.ratsInC):
                        self.cdone = True
                elif self.ratsInB == 2:
                    if combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.cdone,
                              self.ratsInC) and combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack,
                                                       self.cdone, self.ratsInC):
                        self.cdone = True
                elif self.ratsInC == 3:
                    if combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.cdone,
                              self.ratsInC) and combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack,
                                                       self.cdone, self.ratsInC) and combat(self.pHealth, self.pAttack,
                                                                                            "rat", self.rHealth,
                                                                                            self.rAttack, self.cdone,
                                                                                            self.ratsInC):
                        self.cdone = True
                print("""


                                               text here





                                               [1] Look around the room.
                                               [2] Go to the next room.
                                               [3] Go back a room.


                                               """)

                try:
                    r3Num2 = int(input("Your response: "))
                except ValueError:
                    print("Your response can not be a string; try a number.")
                    r3Num2 = input("Your response: ")

                if int(r3Num2) > 3 or int(r3Num2) < 1:
                    print("Your response can not be more than 3 or less than 0")
                    try:
                        r3Num2 = int(input("Your response: "))
                    except ValueError:
                        print("Your response can not be a string; try a number.")
                        r3Num2 = input("Your response: ")

                if r3Num2 == 1:
                    print("""













                                                   desc of room
                                                   """)
                    time.sleep(2)

                    print("""


                                                   text here





                                                   [2] Go to the next room.
                                                   [3] Go back a room.


                                                   """)

                    try:
                        r3Num2 = int(input("Your response: "))
                    except ValueError:
                        print("Your response can not be a string; try a number.")
                        r3Num2 = input("Your response: ")

                    if int(r3Num2) > 3 or int(r3Num2) < 1:
                        print("Your response can not be more than 3 or less than 0")
                        try:
                            r3Num2 = int(input("Your response: "))
                        except ValueError:
                            print("Your response can not be a string; try a number.")
                            r3Num2 = input("Your response: ")
                    if r3Num2 == 2:
                        self.d()
                    elif r3Num2 == 3:
                        self.b()
                elif r3Num2 == 2:
                    self.d()
                elif r3Num2 == 3:
                    self.b()

    def d(self):
        if self.ddone:
            self.dnorat()
        else:
            print("There are " + str(self.ratsInD) + "rats...")
            print("""  



                            It's fightin' time!

                                    [1] Run
                                    [2] Fight!
                                                """)

            try:
                r4num = int(input("Your response: "))
            except ValueError:
                print("Your response can not be a string; try a number.")
                r4num = input("Your response: ")

            if int(r4num) > 2 or int(r4num) < 1:
                print("Your response can not be more than 2 or less than 0")
                try:
                    r4num = int(input("Your response: "))
                except ValueError:
                    print("Your response can not be a string; try a number.")
                    r4num = input("Your response: ")

            if r4num == 1:
                print("The traveler tries to run back a room...")
                if miss(-20, 20):
                    print("The traveler succeeds!")
                    self.cnorat()
                else:
                    if self.ratsInD == 1:
                        if combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.ddone,
                                  self.ratsInD):
                            self.ddone = True
                    elif self.ratsInD == 2:
                        if combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.ddone,
                                  self.ratsInD) and combat(self.pHealth, self.pAttack, "rat", self.rHealth,
                                                           self.rAttack,
                                                           self.ddone, self.ratsInD):
                            self.ddone = True
                    elif self.ratsInD == 3:
                        if combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.ddone,
                                  self.ratsInD) and combat(self.pHealth, self.pAttack, "rat", self.rHealth,
                                                           self.rAttack,
                                                           self.ddone, self.ratsInD) and combat(self.pHealth,
                                                                                                self.pAttack,
                                                                                                "rat", self.rHealth,
                                                                                                self.rAttack,
                                                                                                self.ddone,
                                                                                                self.ratsInD):
                            self.ddone = True
            elif r4num == 2:
                if self.ratsInD == 1:
                    if combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.ddone, self.ratsInD):
                        self.ddone = True
                elif self.ratsInB == 2:
                    if combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.ddone,
                              self.ratsInD) and combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack,
                                                       self.ddone, self.ratsInD):
                        self.ddone = True
                elif self.ratsInD == 3:
                    if combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.ddone,
                              self.ratsInD) and combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack,
                                                       self.ddone, self.ratsInD) and combat(self.pHealth, self.pAttack,
                                                                                            "rat", self.rHealth,
                                                                                            self.rAttack, self.ddone,
                                                                                            self.ratsInD):
                        self.ddone = True
                print("""


                                                           text here





                                                           [1] Look around the room.
                                                           [2] Go back a room.


                                                           """)

                try:
                    r4num2 = int(input("Your response: "))
                except ValueError:
                    print("Your response can not be a string; try a number.")
                    r4num2 = input("Your response: ")

                if int(r4num2) > 2 or int(r4num2) < 1:
                    print("Your response can not be more than 2 or less than 0")
                    try:
                        r4num2 = int(input("Your response: "))
                    except ValueError:
                        print("Your response can not be a string; try a number.")
                        r4num2 = input("Your response: ")

                if r4num2 == 1:
                    print("""













                                                               desc of room
                                                               """)
                    time.sleep(2)

                    print("""


                                                               text here





                                                        
                                                               [2] Go back a room.


                                                               """)

                    try:
                        r4num2 = int(input("Your response: "))
                    except ValueError:
                        print("Your response can not be a string; try a number.")
                        r4num2 = input("Your response: ")

                    if int(r4num2) > 2 or int(r4num2) < 1:
                        print("Your response can not be more than 2 or less than 0")
                        try:
                            r4num2 = int(input("Your response: "))
                        except ValueError:
                            print("Your response can not be a string; try a number.")
                            r4num2 = input("Your response: ")
                    if r4num2 == 2:
                        self.c()
                elif r4num2 == 2:
                    self.c()

    def locked(self):
        if self.hasGrain:
            pass
        else:
            pass

    def anorat(self):
        if not self.hasKey:
            print("""
    
    
                       text here
    
    
    
    
    
                       [1] Look around the room.
                       [2] Go to the next room.
    
    
                       """)

            try:
                r1Num2 = int(input("Your response: "))
            except ValueError:
                print("Your response can not be a string; try a number.")
                r1Num2 = input("Your response: ")

            if int(r1Num2) > 2 or int(r1Num2) < 1:
                print("Your response can not be more than 2 or less than 0")
                try:
                    r1Num2 = int(input("Your response: "))
                except ValueError:
                    print("Your response can not be a string; try a number.")
                    r1Num2 = input("Your response: ")

            if r1Num2 == 1:
                print("""
    
    
    
    
    
    
    
    
    
    
    
    
    
                           The room has nothing in it but a locked door, a hallway to the next room, and a hole in 
                           the wall. """)

                print("""
    
    
                           text here
    
    
    
    
    
                           [2] Go to the next room.
    
    
                           """)

                try:
                    r1Num2 = int(input("Your response: "))
                except ValueError:
                    print("Your response can not be a string; try a number.")
                    r1Num2 = input("Your response: ")

                if int(r1Num2) > 2 or int(r1Num2) < 1:
                    print("Your response can not be more than 2 or less than 0")
                    try:
                        r1Num2 = int(input("Your response: "))
                    except ValueError:
                        print("Your response can not be a string; try a number.")
                        r1Num2 = input("Your response: ")
                if r1Num2 == 2:
                    self.b()
            elif r1Num2 == 2:
                self.b()
        else:
            print("""


                       text here





                       [1] Look around the room.
                       [2] Go to the next room.
                       [3] Go into the locked room.


                       """)

            try:
                r1Num2 = int(input("Your response: "))
            except ValueError:
                print("Your response can not be a string; try a number.")
                r1Num2 = input("Your response: ")

            if int(r1Num2) > 2 or int(r1Num2) < 1:
                print("Your response can not be more than 2 or less than 0")
                try:
                    r1Num2 = int(input("Your response: "))
                except ValueError:
                    print("Your response can not be a string; try a number.")
                    r1Num2 = input("Your response: ")

            if r1Num2 == 1:
                print("""













                           The room has nothing in it but a locked door, a hallway to the next room, and a hole in 
                           the wall. """)

                print("""


                           text here





                           [2] Go to the next room.
                           [3] Go into the locked room.


                           """)

                try:
                    r1Num2 = int(input("Your response: "))
                except ValueError:
                    print("Your response can not be a string; try a number.")
                    r1Num2 = input("Your response: ")

                if int(r1Num2) > 2 or int(r1Num2) < 1:
                    print("Your response can not be more than 2 or less than 0")
                    try:
                        r1Num2 = int(input("Your response: "))
                    except ValueError:
                        print("Your response can not be a string; try a number.")
                        r1Num2 = input("Your response: ")
            elif r1Num2 == 2:
                self.b()
            elif r1Num2 == 3:
                self.locked()

    def bnorat(self):
        print("""


                   text here





                   [1] Look around the room.
                   [2] Go to the next room.
                   [3] Go back a room.


                   """)

        try:
            r2Num2 = int(input("Your response: "))
        except ValueError:
            print("Your response can not be a string; try a number.")
            r2Num2 = input("Your response: ")

        if int(r2Num2) > 3 or int(r2Num2) < 1:
            print("Your response can not be more than 3 or less than 0")
            try:
                r2Num2 = int(input("Your response: "))
            except ValueError:
                print("Your response can not be a string; try a number.")
                r2Num2 = input("Your response: ")

        if r2Num2 == 1:
            print("""













                       desc of room
                       """)
            time.sleep(2)

            print("""


                       text here





                       [2] Go to the next room.
                       [3] Go back a room.


                       """)

            try:
                r2Num2 = int(input("Your response: "))
            except ValueError:
                print("Your response can not be a string; try a number.")
                r2Num2 = input("Your response: ")

            if int(r2Num2) > 3 or int(r2Num2) < 1:
                print("Your response can not be more than 3 or less than 0")
                try:
                    r2Num2 = int(input("Your response: "))
                except ValueError:
                    print("Your response can not be a string; try a number.")
                    r2Num2 = input("Your response: ")
            if r2Num2 == 2:
                self.c()
            elif r2Num2 == 3:
                self.a()
        elif r2Num2 == 2:
            self.c()
        elif r2Num2 == 3:
            self.a()

    def cnorat(self):
        print("""


                   text here





                   [1] Look around the room.
                   [2] Go to the next room.
                   [3] Go back a room.


                   """)

        try:
            r3Num2 = int(input("Your response: "))
        except ValueError:
            print("Your response can not be a string; try a number.")
            r3Num2 = input("Your response: ")

        if int(r3Num2) > 3 or int(r3Num2) < 1:
            print("Your response can not be more than 3 or less than 0")
            try:
                r3Num2 = int(input("Your response: "))
            except ValueError:
                print("Your response can not be a string; try a number.")
                r3Num2 = input("Your response: ")

        if r3Num2 == 1:
            print("""













                       room desc
                       """)
            time.sleep(2)

            print("""


                       text here





                       [2] Go to the next room.
                       [3] Go back a room


                       """)

            try:
                r3Num2 = int(input("Your response: "))
            except ValueError:
                print("Your response can not be a string; try a number.")
                r3Num2 = input("Your response: ")

            if int(r3Num2) > 3 or int(r3Num2) < 1:
                print("Your response can not be more than 3 or less than 0")
                try:
                    r3Num2 = int(input("Your response: "))
                except ValueError:
                    print("Your response can not be a string; try a number.")
                    r3Num2 = input("Your response: ")
            if r3Num2 == 2:
                self.d()
            elif r3Num2 == 3:
                self.b()
        elif r3Num2 == 2:
            self.d()
        elif r3Num2 == 3:
            self.b()

    def dnorat(self):
        print("""


                   text here





                   [1] Look around the room.
                   [2] Go back a room.


                   """)

        try:
            r4Num2 = int(input("Your response: "))
        except ValueError:
            print("Your response can not be a string; try a number.")
            r4Num2 = input("Your response: ")

        if int(r4Num2) > 2 or int(r4Num2) < 1:
            print("Your response can not be more than 2 or less than 0")
            try:
                r4Num2 = int(input("Your response: "))
            except ValueError:
                print("Your response can not be a string; try a number.")
                r4Num2 = input("Your response: ")

        if r4Num2 == 1:
            print("""













                       room desc
                       """)
            time.sleep(2)

            print("""


                       text here





                       [2] Go back a room


                       """)

            try:
                r4Num2 = int(input("Your response: "))
            except ValueError:
                print("Your response can not be a string; try a number.")
                r4Num2 = input("Your response: ")

            if int(r4Num2) > 2 or int(r4Num2) < 1:
                print("Your response can not be more than 2 or less than 0")
                try:
                    r4Num2 = int(input("Your response: "))
                except ValueError:
                    print("Your response can not be a string; try a number.")
                    r4Num2 = input("Your response: ")
            if r4Num2 == 2:
                self.c()
        elif r4Num2 == 2:
            self.c()


class Game:
    def __init__(self):
        self.room = Room()
        print("""





















    







    """)

        print("Greetings, traveler!")
        time.sleep(2.3)
        print("""
        You find yourself in the village of West Valdensmear, nestled in the forest of HEEEEEEEG.
        You see an old well in the center, next to which leans an old man. Surrounding this are several
        small hovels, an old church, and directly across from you, a ramshackle old building with a 
        wooden shingle hanging out front which reads, 'The Groggy Dog.'
        """)
        time.sleep(10)
        print("""
            Crossing through the town center, you enter the tavern.
        """)
        time.sleep(2.7)
        print("""
            An elderly half-orc greets you at the door, feebly waving his lumpy greenish arms.
                'Finally! Are you here about the rats!? Thank you, thank you! I'd take care of the buggers myself,
                 but I've seen too many winters!'
        """)
        time.sleep(8)
        print("""
            He gestures you frantically toward a rickety wooden basement door.
        """)

    def run(self):
        self.room.a()


if __name__ == "__main__":
    game = Game()
    game.run()
