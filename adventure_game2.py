import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(3)

def start_game():
    beast = random.choice(["Dragon", "Drake" , "Ogre" , "Demon" , "Giant Snake" , "Giant Spider"])
    
    intro()
    room_1(beast)
    
    
def intro():
    print_pause("After years of looking you finally found it.")
    print_pause("The cave of legends, where the great artifacts of the old world are hidden.")
    print_pause("You know you must go into the cave but it is said to be guarded by a great beast.")
    print_pause("You are not a fighter just a explorer with little to fight with.")
    print_pause("You know you must enter regardless of the danger, so you press on past the opening and into the dark.")


def room_1(beast):
    print_pause("As you enter the first room you notice it is filled with skeletons and signs of a " + beast + ".")
    print_pause("The room seems to be empty on first glance but something catches your eye.")
    print_pause("It seems to call to you, like a whisper telling you to grab it.")
    print_pause("You've never encountered something like this, so you appoarch the object.")
    while True:
        answer = input("Do you take the object? [Yes/No]\n")
    

        if answer == "Yes":
            print_pause("As you grab the item you notice a darkness come out of it, the object object seems to have cursed you.")
            print_pause("You fall to the floor losing control of your body as the darkness covers you.")
            print_pause("You know this is the ended, you have failed.")
            answer = input("Would you like to try again? [Yes/No]\n")


            if answer == "Yes":
                print_pause("Good im glad to hear that, starting the game over now.")
                start_game()
                break

    
            else:
                print_pause("Goodbye and thank you for playing, I hope you enjoyed it!!!")
                break


        elif answer == "No":
            print_pause("You know better than to grab an object like that only bad omens come from a thing like that.")
            print_pause("You notice a new room to the right  as you walk away.")
            print_pause("It seems to be the only way forward so you press on.")
            room_2()
            break


        else:
            print_pause("Invalid answer please try again.")

    
def room_2():
    print_pause("As you enter this room you see that this room is massive and filled with gold and treasure.")
    print_pause("You are looking for a crown, the crown of the first king.")
    print_pause("You look over the room a few times and you see a chest in the corner of the room.")
    print_pause("It has the engraving of the old kingdom, you know this has to be where the crown is.")
    print_pause("You walk up to the chest, you find a sword and the crown inside under all the jewels and coins inside.")
    print_pause("As you grab both of the items you hear a faint whisper say \"A theif in my chamber\"")
    print_pause("You are confused by this voice an know you must leave you turn around and notice the enterance is gone.")
    print_pause("As you look around you see a door to the left and a door to the right.")
    while True:
        answer = input("Which door will you go through [Left/Right]\n")


        if answer == "Left":
            print_pause("As you enter this room something feels off but you press on to the next chamber that is very large with tunnels along the walls.")
            print_pause("This chamber looks safe.")
            room_3()
            break


        elif answer == "Right":
            print_pause("As you enter this room you can see a light to the outside, you feel relived knowing you are almost out.")
            print_pause("You walk to the light but just a you get to it the floor gives out and you fall into a spike pit.")
            print_pause("You are now stuck with no way out and have failed.")
            answer = input("Would you like to try again? [Yes/No]\n")
        
        
            if answer == "Yes":
                print_pause("Good im glad to hear that, starting the game over now.")
                start_game()
                break
    
        
            else:
                print_pause("Goodbye and thank you for playing, I hope you enjoyed it!!!")
                exit()
    
    
        else:
            print_pause("Sorry invaild answer please try again.")


def room_3():
    print_pause("As you enter this room you notice that the air is stale in hear and very cold.")
    print_pause("As you look around you notice the light shining through the crack of one of the tunnels so you appoarch it.")
    print_pause("When you get about half way to the room you hear a loud crash behind you.")
    print_pause("You turn to face the noise and notice its the beast that matchs the marks from the enterance")
    print_pause("It looks at you an says \"Look thief I know you have what is mine return what you have taken and i will spare you\" ")
    print_pause("They continue\"Or you can fight me and you my fight me for a chance for it all.\" ")
    print_pause("You think about it for a second and relise you must either run or fight the beast.")
    while True:
        answer = input("Which do you choose? [Fight/Run]\n")



        if answer == "Fight":
            print_pause("You yell at the beast that you will fight and they gladly accept.")
            print_pause("You put up a good effort with your new sword but fail in the end it has defeated you.")
            answer = input("Would you like to try again? [Yes/No]\n")
        
        
            if answer == "Yes":
                print_pause("Good im glad to hear that, starting the game over now.")
                start_game()
                break
    
        
            else:
                print_pause("Goodbye and thank you for playing, I hope you enjoyed it!!!")
                break
                
                
        elif answer == "Run":
            print_pause("You say you will return the items and it looks away for one second and you make a dash for the light.")
            print_pause("You almost get hit by its swing but manage to avoid it making it pass the fowl creature and into the tunnel")
            print_pause("You crawal to the end and have escaped the cave.")
            print_pause("You have won!!!!")
        

            answer = input("Would you like to play again [Yes/No]\n")


            if answer == "Yes":
                print_pause("Thank you for playing and congarts on winning, I hope you have fun this on this next playthrough!!")
                start_game()


            else:
                print_pause("Thank you for playing the game and congrats on winning. I hope you try it again sometime.")


        else:
            print_pause("Sorry invaild answer please try again.")

    
start_game()