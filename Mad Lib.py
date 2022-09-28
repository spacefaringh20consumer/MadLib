# This is my Mad Lib project. Enjoy!

# Created by hydr0, last updated on 9/27/2022

# The loop allows the Mad Lib to be played up to three times.

loop = 1

while loop < 3:
    # Questions for the Mad Lib
    print("Answer the following questions and your responses will be put into a Mad Lib!")

    noun = input("Choose a noun: ")

    noun2 = input("Choose a second noun: ")

    noun3 = input("Choose a third noun: ")

    plural = input("Choose a plural noun: ")

    verb = input("Choose a verb: ")

    verb2 = input("Choose a second verb: ")

    name = input("Choose a name: ")

    adj = input("Choose an adjective: ")

    loc = input("Choose a popular location: ")

    # Previous inputs will be plugged into the predetermined phrases below

    print("What a beautiful day in " + loc + "! Wait, is that a " + noun3 + " in the sky?")

    print("You turn to your left to see a " + adj + " " + noun2 + " " + verb + " towards you.")

    print(name + "! Where are my " + plural + "?!")

    print(name + " " + verb2 + " out of the way!")

    print("I wouldn't have to " + verb2 + " if I had my " + noun + " and you had your " + plural + "!")

    print("Luckily, you and " + name + " quickly " + verb2 + " out of the way!")

    print("What an eventful day in " + loc + ", and an exhausting one too!")

    loop += 1

    # Thanks for playing!
