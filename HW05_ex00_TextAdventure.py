#!/usr/bin/env python
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
import sys

# Body


def infinite_stairway_room(user,count=0):
    print "%s walk through the door to see a dimly lit hallway." %user
    print "At the end of the hallway is a", count * 'long ', 'staircase going towards some light'
    next = raw_input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print '%s take the stairs'%user
        if (count > 0):
            print "but you're not happy about it"
        infinite_stairway_room(user,count + 1)
    # option 2 == ?????
    if next == "run":
        dead("Try again")
        


def gold_room(user):
    print "This room is full of gold.  How much do you take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        try:
            how_much = int(next)
        except:
            dead("Man, learn to type a number.")
        else:
            if how_much < 50:
                print "Nice, you're not greedy, you win!"
                exit(0)
    else:
        dead("You greedy bastard!")


def bear_room(user):
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How is %s going to move the bear?" %user
    bear_moved = False

    while True:
        next = raw_input(">")

        if ("take" in next) or ("honey" in next) :
            dead("The bear looks at you then slaps your face off.")
        elif ("taunt" in next) and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif "taunt" in next and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif (("open" in next) or("door" in next)) and bear_moved:
            gold_room(user)
        else:
            print "I got no idea what that means."


def cthulhu_room(user):
    print "Here ,%s you see the great evil Cthulhu." %user
    print "He, it, whatever stares at %s and you go insane." %user
    print "Do you, %s flee for your life or eat your head?" %user

    next = raw_input(">")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room(user)


def dead(why):
    print why, "Good job!"
    exit(0)


##############################################################################
def main():
    # START the TextAdventure game
    #print "What is your name?.."
    user = sys.argv[1]
    print user  + ",you are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("Enter left or right ")

    if next == "left":
        bear_room(user)
    elif next == "right":
        cthulhu_room(user)
    elif next=="up":
        infinite_stairway_room(user)
    else:
        dead("You stumble around the room until you starve.")

if __name__ == '__main__':
    main()
