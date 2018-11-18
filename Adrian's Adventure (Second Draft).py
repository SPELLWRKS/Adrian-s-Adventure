#Adrian Spelling
#November 16, 2018
#Lesson 6 Discussion

#Adrian's Quest

#This program is a simple text-based game. The user enters their name
#and is randomly assigned 1 of 3 roles: Knight, Mage or Barbarian. The user is
#then given the option to choose between 3 paths: left, right or middle.
#The ending to the game is based on the user's choice.


#imports the random function 
import random

#the main function
def main():
    #initializes all variables
    playAgain = "yes"
    characterName = 'NO NAME'
    characterTrait = 0
    choice = True
    role = 'none'

    title()
    #this loop resets all variables based on user input
    while playAgain == "yes":
        characterName = name(characterName) #calls the characterName function
        characterTrait = 0
        role = assignRole(characterName, characterTrait) #calls the assignRole function
        choice = path(characterName, choice) #calls the path function
        playAgain = reset(playAgain)
        if playAgain == False:
            print('Invalid entry! Please enter "yes" or "no: :')


#prints the game's title
def title():
    print("W=A=R=R=I=O=R Q=U=E=S=T")
    print('-•-•-•-•-•-•-•-•-•-•-•-')
    print('--By: Adrian Spelling--')
    print('')#prints a blank line

        

#this function stores the user's name as a variable for later use
def name(characterName):
    print('')
    characterName = str(input("Welcome warrior! What is your name?: "))
    return characterName


#this function assigns a random role to the user, based on 3 possible outcomes
#utilizing the random function. These roles assigned using an if-elif statement
def assignRole(characterName, characterTrait):
    characterTrait = random.randint(1, 3)
    if characterTrait == 1:
        print('')
        print(characterName + ", you have been chosen as a Knight!\nYou must find and rescue the princess!")
    elif characterTrait == 2:
        print('')
        print(characterName + ", you have been chosen as a Mage!\nYou must find and rescue the princess!")
    elif characterTrait == 3:
        print('')
        print(characterName + ", you have been chosen as a Barbarian!\nYou must find and rescue the princess!")
    return characterName, characterTrait


#this function allows the user to choose a path, determining the end of the game
#if the user chooses the "middle" option, the characterName variable is called
def path(characterName, choice):
    print('')
    choice = str(input("You stand in front of three paths,which will you take?\n(choose: left, middle or right): "))    
    if choice == "left":
        print('')
        print("You have chosen the left path.\nA bear has attacked you and you have died!")
    elif choice == "middle":
        print('')
        print("You have chosen the middle path.\n☆☆☆YOU HAVE FOUND THE PRINCESS!!!☆☆☆\nExcellent Job, " + characterName +"!")
    elif choice == "right":
        print('')
        print("You have chosen the right path.\nYou fall into a pit from which there is no escape!")
    else:
        print('')
        print('Invalid entry. Please enter "left", "middle" or "right": ')
    return choice


def reset(playAgain):
    print('')
    playAgain = str(input("Would you like to play again (yes or no)?: "))
    if playAgain == "yes":
        print('')
        print("Your adventure begins again!")
    elif playAgain == "no":
        print('')
        print("Goodbye for now!")
    else:
        playAgain == False
    return playAgain
    

        

main()
