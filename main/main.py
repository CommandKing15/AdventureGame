import time

if __name__ == "__main__":
    print("""                  
     /\      | |               | |                  
    /  \   __| |_   _____ _ __ | |_ _   _ _ __ ___  
   / /\ \ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ 
  / ____ \ (_| |\ V /  __/ | | | |_| |_| | | |  __/ 
 /_/    \_\__,_| \_/_\___|_| |_|\__|\__,_|_|  \___| 
                / ____|                             
               | |  __  __ _ _ __ ___   ___         
               | | |_ |/ _` | '_ ` _ \ / _ \        
               | |__| | (_| | | | | | |  __/        
                \_____|\__,_|_| |_| |_|\___|    
                
        Created By: [@]* and Cr@sh Override
        
        *aKa CommandKing15
        
        Please pick a story
        
        [1] - The Rats of the Groggy Dog!
            - GrugBug the Half-Orc is having trouble in the basement of his tavern,'The Groggy Dog.'
              Massive rats have taken residence and are eating his supplies; he has asked for your help!
        
        **[2] - In the Cave of the Goblin King!
            - Residents of the village are under siege! Missing crops, stolen pets, and spooky noises at night!
              The Chief of the town, Phthnemod Mon, believes goblins from a cave nearby are to blame.
        
        **[3] - The Poisoned Well!
            - The village's water supply has fallen prey to some bizarre ailment. Those who drink from it become
              perilously ill. Krek, the town's crazy old man, has an idea of what might be the cause... 
              
              
              **Not done will crash!
    """)
    try:
        storyNum = int(input("Your response: "))
        #storyNum = 1
    except ValueError:
        print("Your response can not be a string; try a number.")
        storyNum = input("Your response: ")

    if int(storyNum) > 3 or int(storyNum) < 1:
        print("Your response can not be more than 3 or less than 0")
        try:
            storyNum = int(input("Your response: "))
        except ValueError:
            print("Your response can not be a string; try a number.")
            storyNum = input("Your response: ")

    if storyNum == 1:
            print("You have selected to start story 1...")
            time.sleep(0.3)
            print("Transferring...")
            exec(open("resources/storyLn1.py").read())

    elif storyNum == 2:
            print("You have selected to start story 2...")

            time.sleep(0.3)

            print("Transferring...")

            exec(open("resources/storyLn2.py").read())

    elif storyNum == 3:
            print("You have selected to start story 3...")

            time.sleep(0.3)

            print("Transferring...")

            exec(open("resources/storyLn3.py").read())
