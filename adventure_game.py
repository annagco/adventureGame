import sys
import time
import random
items = []
weapon = random.choice(["deadly solar lazer",
                        "powerful and dangerous life crystal"])


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(3)


def intro():
    print_pause("You wake up in a bright room and you can't seem to"
                " remember why you are there, or even where you are.")
    print_pause("You are lying on a cold, metal table.")
    print_pause("You stand up and look around. "
                "You see two big doors: a white door and a black door.")
    print_pause("Each door has an alien symbol, "
                "but you dont know what they mean.")


def first_act():
    print_pause("Would you like to:")
    choice = input("1. Search the room for a key\n"
                   "2. Go straight to the doors\n")
    if choice == "1":
        print_pause("You look around the room and find "
                    "an unsual shaped key under the table.")
        print_pause("You notice that the symbol on each door is also"
                    " on the key so you put the key in your pocket.")
        items.append("Key")
    elif choice == "2":
        print_pause("You run towards the doors and try to open them,"
                    " but they're locked shut.\n"
                    "Well... there must be a key somewhere in this room.")
        first_act()
    else:
        print_pause("Please choose: 1 or 2.")
        first_act()


def second_act():
    if "Key" in items:
        print_pause("You go towards the doors,"
                    " hesitant to open one of them.")
        print_pause("Which door will you open first:")
        door = input("1. The White door\n"
                     "2. The Black door\n")
        if door == "1":
            print_pause("You turn the key in the lock and "
                        "the door slowly opens.")
            print_pause("You look around cautiously and hear "
                        "a very loud buzz in your ears.")
            print_pause("You fall to the ground and see five huge alien-like"
                        " creatures approach and pick you up.")
            print_pause("They take you back to the table in the"
                        " white room and tie you down.")
            print_pause("The last thing you remember seeing was a very tall, "
                        "alien with huge slanted eyes making loud noises "
                        "you couldn't understand.")
            print_pause("You wake up with a key in your pocket and walk "
                        "towards the doors.")
            second_act()
        elif door == "2":
            print_pause("The door was jammed, but after a few kicks it opened."
                        " Luckily there was no one on the other side.")
            print_pause("You find yourself in a small, dark room. "
                        "Looks like an office.")
            print_pause("You open all of the drawers until you find some sort"
                        " of weapon. It was a {}.".format(weapon))
            print_pause("You put the {} with the key and go back"
                        " to the bright room and face the "
                        "white door.".format(weapon))
            items.append(weapon)
        else:
            print_pause("Please choose: 1 or 2.")
            second_act()


def inbetween():
    print_pause("You gather courage to go through the white door.")
    print_pause("You think to yourself \"What could be in there?\"")
    print_pause("You turn the key and unlock the white door.")
    print_pause("There were panels and lights flickering everywhere.")
    print_pause("You became confused, but walked around the room. Suddenly, "
                "five tall, thin aliens see you and walk in your direction.")


def third_act():
    final_choice = input("Do you:\n"
                         "1. Point the {} at them threateningly and demand"
                         " that they take you back to earth\n"
                         "2. Run away and hope they don't "
                         "take you\n".format(weapon))
    if final_choice == "1":
        print_pause("The aliens start making very loud noises and panic! "
                    "One of them runs towards some sort of device and "
                    "back to you.")
        print_pause("It was a translating device!")
        print_pause("\"Please, mortal human. Give us the {} and we will "
                    "honor your demand. We will take you back. "
                    "Please!\"".format(weapon))
        print_pause("\"We mean you no harm. Please. We will do as you wish.\"")
        print_pause("You hesitate at first, "
                    "then you give the {} to them.".format(weapon))
        print_pause("They start making calm noises and show you that they"
                    " will in fact take you back home.")
        print_pause("Moments later you wake up, jumping out of your bed "
                    "terrified and sweaty.")
        print_pause("You look around and you are in your room.")
        print_pause("You try to calm yourself down and laugh thinking it was"
                    " all just a crazy dream.")
        print_pause("But... you reach in your pocket and find the key...")
        print_pause("... was it real?")
        play_again()
    elif final_choice == "2":
        print_pause("You attempt to run away, but before you can get "
                    "to the door, one of the aliens block you.")
        print_pause("You run around the room until another alien caught you.")
        print_pause("They all grab onto your arms and start making loud"
                    " buzzing noises in your ears.")
        print_pause("You feel immense pressure in your head and can't stand "
                    "the pain. You faint slowly until you are dragged back to"
                    " the table.")
        print_pause("This time... you don't wake up.")
        play_again()
    else:
        print_pause("Please choose: 1 or 2.")


def play_again():
    replay = input("Would you like to play again? (y/n)")
    if replay == "y":
        print_pause("Very well! Good luck!")
        play_game()
    elif replay == "n":
        print_pause("Ok! See you again soon!")
        sys.exit(0)
    else:
        print_pause("Please answer with y for yes or n for no.")


def play_game():
    intro()
    first_act()
    second_act()
    inbetween()
    third_act()
    play_again()


play_game()
