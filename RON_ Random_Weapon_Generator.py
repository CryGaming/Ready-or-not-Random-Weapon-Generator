import random

def gear():
    print("You have chosen gear! Please press 1 for armor or 2 for headwear")
    choice2 = int(input())
    if choice2 == 1:
        rannum = int(random.random() * 3)
        print("You have chosen Armor with your number being " + str(rannum))
    else:
        rannum = int(random.random() * 5)
        print("You have chosen Headwear with your number being " + str(rannum))

def grenade():
    rannum = int(random.random() * 3)
    print("Your random grenade is number " + str(rannum))

def lTac():
    print("You have Chosen Long Tactical")
    rannum = int(random.random() * 7)
    print("Your randomly selected Long Tactical is #" + str(rannum))

def pGun():
    print("You have selected Primary Weapon! Please press 1 for Assualt, 2 for Submachine Gun, 3 for Shotgun, 4 for Launcher, 5 for all")
    choice2 = int(input())
    if choice2 == 1:
        rannum = int(random.random() * 11)
        print("Your randomly generated Assualt Rifle is number: " + str(rannum))
    else:
        if choice2 == 2:
            rannum = int(random.random() * 3)
            print("Your randomly chosen Submachine Gun is :" + str(rannum))
        else:
            if choice2 == 3:
                rannum = int(random.random() * 3)
                print("Your randomly generated shotgun is" + str(rannum))
            else:
                if choice2 == 4:
                    print("Good luck, you have chosen the M32A1 Flash")
                else:
                    if choice2 == 5:
                        rannum = int(random.random() * 18)
                        print("Congratulations! You have picked weapon #" + str(rannum))

def sGun():
    print("You have chosen Secondary Weapons")
    rannum = int(random.random() * 7)
    print("Your randomly chosen sidearm is #" + str(rannum))

def tacdev():
    rannum = int(random.random() * 4)
    print("You have chosen Tactical Devices with your randomly chosen option being number " + str(rannum))

# Main
weapChoice = 0
print("Hello and welcome to the Weapon generator!")
print("Please press a number to Generate your loadout! (Only works for Ready or Not) 1= primary, 2= secondary, 3= Long Tacticle, 4=grenade, 5=Tactical Device,")
weapChoice = int(input())
while weapChoice != -1:
    if weapChoice == 1:
        pGun()
    else:
        if weapChoice == 2:
            sGun()
        else:
            if weapChoice == 3:
                lTac()
            else:
                if weapChoice == 4:
                    gear()
                else:
                    if weapChoice == 5:
                        grenade()
                    else:
                        if weapChoice == 6:
                            tacdev()
    print("You have reached the end of the program, Please choose again or press -1 to quit the program. 1 for Primary, 2 for Secondary, 3 for Long Tactical, 4 for gear,5 for grenade, 6 for tacdev")
    weapChoice = int(input())
