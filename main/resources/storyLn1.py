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
                    print("You attacked the diggity-dang " + str(enemyN) + " and it has " + str(enemyH) + " HP left...")
            else:
                print("You missed!")
    return playerH


class Room:
    def __init__(self):
        self.rHealth = radn(10)
        self.rAttack = radn(2)
        self.aHealth = radn(15)
        self.aAttack = radn(4)
        self.pHealth = radn(25)
        self.pAttack = radn(5)
        self.ratsInB = random.randint(1, 3)
        self.ratsInC = random.randint(1, 3)
        self.ratsInD = random.randint(1, 3)
        self.adone = True
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
                self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.adone, 1)
                if self.pHeatlh > 0:
                    self.adone = True

                print("""
                
                
                Wow! What a rat fight! The little toother sure did bite! But you done smacked it.
                
                
                
                
                
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
    
    
                    Wow! What a rat fight! The little toother sure did bite! But you done smacked it.
                    And what a goopy rat mess you've made! Onward, brave traveler, toward who knows how many
                    more bite-crazed rodents!
                
    
    
    
    
    
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
            print("There are " + str(self.ratsInB) + " stinking little filthy awesome rats...")
            print(""" It's rat fightin' time, big boy!

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
                        self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.bdone,
                                              self.ratsInB)
                        if self.pHeatlh > 0:
                            self.bdone = True
                    elif self.ratsInB == 2:
                        self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.bdone,
                                              self.ratsInB)
                        self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth,
                                              self.rAttack, self.bdone, self.ratsInB)
                        if self.pHeatlh > 0:
                            self.bdone = True
                    elif self.ratsInB == 3:
                        self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.bdone,
                                              self.ratsInB)
                        self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth,
                                              self.rAttack, self.bdone, self.ratsInB)
                        self.pHeatlh = combat(self.pHealth,
                                              self.pAttack,
                                              "rat",
                                              self.rHealth,
                                              self.rAttack,
                                              self.bdone,
                                              self.ratsInB)
                        if self.pHeatlh > 0:
                            self.bdone = True
            elif r2Num == 2:
                if self.ratsInB == 1:
                    self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.bdone,
                                          self.ratsInB)
                    if self.pHeatlh > 0:
                        self.bdone = True
                elif self.ratsInB == 2:
                    self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.bdone,
                                          self.ratsInB)
                    self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth,
                                          self.rAttack, self.bdone, self.ratsInB)
                    if self.pHeatlh > 0:
                        self.bdone = True
                elif self.ratsInB == 3:
                    self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.bdone,
                                          self.ratsInB)
                    self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth,
                                          self.rAttack, self.bdone, self.ratsInB)
                    self.pHeatlh = combat(self.pHealth,
                                          self.pAttack,
                                          "rat",
                                          self.rHealth,
                                          self.rAttack,
                                          self.bdone,
                                          self.ratsInB)
                    if self.pHeatlh > 0:
                        self.bdone = True
                print("""


                                   While there may once have been lovely floral-patterned wallpaper in this room,
                                    it has now been replaced with stinking crimson rat blood splatter.
                                    
                                    It really accents the furniture!





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













                            The room has nothing in it but a locked door, a hallway to the next room, a hole in 
                           the wall, and a very nice oil painting of Carl Sagan. My stars!
                                       """)
                    time.sleep(2)

                    print("""


                                    While there may once have been lovely floral-patterned wallpaper in this room,
                                    it has now been replaced with stinking crimson rat blood splatter.
                                    
                                    It really accents the furniture!





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
            print("All up in here, fair traveler, there appear to be " + str(self.ratsInC) + " wriggly rats...")
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
                        self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.cdone,
                                              self.ratsInC)
                        if self.pHeatlh > 0:
                            self.cdone = True
                    elif self.ratsInB == 2:
                        self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.cdone,
                                              self.ratsInC)
                        self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth,
                                              self.rAttack,
                                              self.cdone, self.ratsInC)
                        if self.pHeatlh > 0:
                            self.cdone = True
                    elif self.ratsInC == 3:
                        self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.cdone,
                                              self.ratsInC)
                        self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth,
                                              self.rAttack,
                                              self.cdone, self.ratsInC)
                        self.pHeatlh = combat(self.pHealth,
                                              self.pAttack,
                                              "rat",
                                              self.rHealth,
                                              self.rAttack,
                                              self.cdone,
                                              self.ratsInC)
                        if self.pHeatlh > 0:
                            self.cdone = True
            elif r3Num == 2:
                if self.ratsInC == 1:
                    self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.cdone,
                                          self.ratsInC)
                    if self.pHeatlh > 0:
                        self.cdone = True
                elif self.ratsInB == 2:
                    self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.cdone,
                                          self.ratsInC)
                    self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth,
                                          self.rAttack,
                                          self.cdone, self.ratsInC)
                    if self.pHeatlh > 0:
                        self.cdone = True
                elif self.ratsInC == 3:
                    self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.cdone,
                                          self.ratsInC)
                    self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth,
                                          self.rAttack,
                                          self.cdone, self.ratsInC)
                    self.pHeatlh = combat(self.pHealth,
                                          self.pAttack,
                                          "rat",
                                          self.rHealth,
                                          self.rAttack,
                                          self.cdone,
                                          self.ratsInC)
                    if self.pHeatlh > 0:
                        self.cdone = True
                print("""


                    Oh god! Bits and pieces of rat hair and tender rat meat festoon your battle-sweatened head.
                    Like a horrible ancient lord of rat-slaughter, you rise above the bloody maelstrom.
                    
                    Gross, one little bit got in your mouth! PFFFFT! PFFT!





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













                                    Room description?
                
                        More like room DESKription!
                
                        There is only a desc- i mean, desk in this room.
                
                        Why?
                
                        Let us ponder...
                                                   """)
                    time.sleep(2)

                    print("""


                    Oh god! Bits and pieces of rat hair and tender rat meat festoon your battle-sweatened head.
                    Like a horrible ancient lord of rat-slaughter, you rise above the bloody maelstrom.
                    
                    Gross, one little bit got in your mouth! PFFFFT! PFFT!





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
            print("You walk into an especially dusty, dim, desperate, dire and most UNdesirable room.")
            time.sleep(2)
            print("You see, most eyeballedly, " + str(self.ratsInD) + " darn rats...")
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
                        self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.ddone,
                                              self.ratsInD)
                        if self.pHeatlh > 0:
                            self.hasKey = True
                            self.ddone = True
                    elif self.ratsInD == 2:
                        self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.ddone,
                                              self.ratsInD)
                        self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth,
                                              self.rAttack,
                                              self.ddone, self.ratsInD)
                        if self.pHeatlh > 0:
                            self.hasKey = True
                            self.ddone = True
                    elif self.ratsInD == 3:
                        self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.ddone,
                                              self.ratsInD)
                        self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth,
                                              self.rAttack,
                                              self.ddone, self.ratsInD)
                        self.pHeatlh = combat(self.pHealth,
                                              self.pAttack,
                                              "rat",
                                              self.rHealth,
                                              self.rAttack,
                                              self.ddone,
                                              self.ratsInD)
                        if self.pHeatlh > 0:
                            self.hasKey = True
                            self.ddone = True
            elif r4num == 2:
                if self.ratsInD == 1:
                    self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.ddone,
                                          self.ratsInD)
                    if self.pHeatlh > 0:
                        self.hasKey = True
                        self.ddone = True
                elif self.ratsInD == 2:
                    self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.ddone,
                                          self.ratsInD)
                    self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth,
                                          self.rAttack,
                                          self.ddone, self.ratsInD)
                    if self.pHeatlh > 0:
                        self.hasKey = True
                        self.ddone = True
                elif self.ratsInD == 3:
                    self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth, self.rAttack, self.ddone,
                                          self.ratsInD)
                    self.pHeatlh = combat(self.pHealth, self.pAttack, "rat", self.rHealth,
                                          self.rAttack,
                                          self.ddone, self.ratsInD)
                    self.pHeatlh = combat(self.pHealth,
                                          self.pAttack,
                                          "rat",
                                          self.rHealth,
                                          self.rAttack,
                                          self.ddone,
                                          self.ratsInD)
                    if self.pHeatlh > 0:
                        self.hasKey = True
                        self.ddone = True
                print("""


                        Jeez, who'd've thought fighting rats would be so tiring!
                        And some people do this for fun?
                        
                        Giving one of the rats another good kick, out pops a shiny metal key, with a noise
                        like a bottle cap popping off of a crisp, cool, cola.





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




                A fantastic gallery of lizard sculptures presents itself to you.
                
                Oh, what lovely lizards!
                
                The floor is made of dirt, but dang what wonderful lizards.








                                                               
                                                               """)
                    time.sleep(2)

                    print("""


                                                            Jeez, who'd've thought fighting rats would be so tiring!
                        And some people do this for fun?
                        
                        Giving one of the rats another good kick, out pops a shiny metal key, with a noise
                        like a bottle cap popping off of a crisp, cool, cola.





                                                        
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
            print(
                "This room appears to contain only an old fermentation barrel, that looks to need some kind of grain.")
            time.sleep(1.5)
            print("You walk up to have a closer look but here a growling noise coming from behind you...")
            time.sleep(1.6)
            print("""





                       [1] Investigate the sound...
                       [2] Run in fear


                       """)
            try:
                r5num = int(input("Your response: "))
            except ValueError:
                print("Your response can not be a string; try a number.")
                r5num = input("Your response: ")

            if int(r5num) > 2 or int(r5num) < 1:
                print("Your response can not be more than 2 or less than 0")
                try:
                    r5num = int(input("Your response: "))
                except ValueError:
                    print("Your response can not be a string; try a number.")
                    r5num = input("Your response: ")

            if r5num == 2:
                if miss(-20, 13) == 1:
                    if miss(-20, 5) == 1:
                        print("You ran into a liquid puddle and tripped.")
                        time.sleep(0.5)
                        print("Sadly, you died when you slipped...")
                        time.sleep(2)
                        print("Should have had higher grip shoos I guess.")
                        time.sleep(2)
                        exit(0)
                    else:
                        print("You were able to run your way back upstairs.")
                        time.sleep(2)
                        print("The owner was very mad at you that you could not fix his problem and did not let you "
                              "go back.")
                        time.sleep(2)
                        exit(0)
                else:
                    print("You were not able to find an escape route.")
                    time.sleep(1)
                    print("""





                               [1] Investigate the sound...


                               """)
                    try:
                        r5num = int(input("Your response: "))
                    except ValueError:
                        print("Your response can not be a string; try a number.")
                        r5num = input("Your response: ")

                    if int(r5num) > 2 or int(r5num) < 1:
                        print("Your response can not be more than 2 or less than 0")
                        try:
                            r5num = int(input("Your response: "))
                        except ValueError:
                            print("Your response can not be a string; try a number.")
                            r5num = input("Your response: ")
            elif r5num == 1:
                print("You investigate the sound...")
                time.sleep(2)
                print("As you are looking a raccoon carrying a grain bag in his slobber encrusted mouth, jumps out at "
                      "you.")
                time.sleep(1)
                self.pHeatlh = combat(self.pHeatlh, self.pAttack, "raccoon", self.aHealth, self.aAttack, self.ddone, 1)
                if self.pHeatlh > 0:
                    time.sleep(1)
                    print("You did it!")
                    time.sleep(1)
                    print("You got the grain bag and used it to fix the owners brewing problem!")
                    time.sleep(3)
                    print("""
                    
                        On your victorious walk out of 'the groggy dog' the owner tanks you so much for your service. 
                        He also says, 'You are welcome back anytime, Hero Traveler...'. at that he turns to go back in 
                        but stops and says, 'some other towns could use someone like you. I know someone who has some 
                        goblin problems. You should look in to helping him too.'
                    
                    
                    """)
                    time.sleep(13)
                    print("Thankyou For Playing!")
                    time.sleep(1)
                    print("If you would like to play the other endings or the other stories, restart the game and go "
                          "for it.")
                    time.sleep(1)
                    print("If you would like to get the scource code you can find that "
                          "here:'https://github.com/CommandKing15/AdventureGame'. You can use it in your "
                          "own projects just give CommandKing15 credit for it.")
                    time.sleep(3)
                    print("Thanks to Cr@sh Override for most of the text and [@] for programming this mess.")
                    time.sleep(10)
                    exit(0)

    def anorat(self):
        if not self.hasKey:
            print("""
    
    
                       Ooh! Smashed rat parts! And what's this?
                       Twenty dollars?! Your nephew finally lost a bet!
    
    
    
    
    
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
    
    
                          Ooh! Smashed rat parts! And what's this?
                       Twenty dollars?! Your nephew finally lost a bet!
    
    
    
    
    
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


                       Back into the first room, eh?
                       
                       If you're reading this, you owe your uncle twenty dollars.





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













                           The room has nothing in it but a locked door, a hallway to the next room, a hole in 
                           the wall, and a very nice oil painting of Carl Sagan. My stars!""")

                print("""


                           Back into the first room, eh?
                       
                       If you're reading this, you owe your uncle twenty dollars.





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


                   Dang! Still lookin' for rats to kill, huh?
                   Okay, you do you.
                   
                   Creep.





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

                    Looking around the murky dimness, you see a pile of cowboy hats in one corner.
                    Hanging on the walls are a series of very fashionably festooned mannequins.
                    
                    Ooh what lovely seasonable styles!











                       
                       """)
            time.sleep(2)

            print("""


                       Dang! Still lookin' for rats to kill, huh?
                   Okay, you do you.
                   
                   Creep.





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


                   Rats live on no evil star? 
                   
                   Palindrome THIS you ratless room!





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

                Room description?
                
                More like room DESKription!
                
                There is only a desc- i mean, desk in this room.
                
                Why?
                
                Let us ponder...
                    










                       
                       """)
            time.sleep(2)

            print("""


                       Rats live on no evil star? 
                   
                   Palindrome THIS you ratless room!





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


                  Knock knock!
                  
                  Who's there?
                  
                  Not rats!
                  
                  BWAAAAH BWA BWA BWAAAAAAH!





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

                A fantastic gallery of lizard sculptures presents itself to you.
                
                Oh, what lovely lizards!
                
                The floor is made of dirt, but dang what wonderful lizards.











                       
                       """)
            time.sleep(2)

            print("""


                       Knock knock!
                  
                  Who's there?
                  
                  Not rats!
                  
                  BWAAAAH BWA BWA BWAAAAAAH!





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
