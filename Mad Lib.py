# This is my Mad Lib project. Enjoy!

# Created by hydr0, last updated on 9/29/2022

# The loop allows the Mad Lib to be played up to three times. This also gives three different choices for Mad Libs!

loop = 1

while loop <= 3:
    # Questions for the Mad Lib
    print("Answer the following questions and your responses will be put into a Mad Lib!")

    noun = input("Choose a noun: ").capitalize()

    noun2 = input("Choose a second noun: ").capitalize()

    noun3 = input("Choose a third noun: ").capitalize()

    plural = input("Choose a plural noun: ").capitalize()

    verb = input("Choose a verb: ").capitalize()

    verb2 = input("Choose a second verb: ").capitalize()

    name = input("Choose a name: ").capitalize()

    adj = input("Choose an adjective: ").capitalize()

    loc = input("Choose a popular location: ")

    which_lib = input("Choose which Mad Lib you'd like; [1], [2], or [3]: ")

    # Previous inputs will be plugged into the predetermined phrases below
    if which_lib == "1":

        print("What a beautiful day in " + loc + "! Wait, is that a " + noun3 + " in the sky?")

        print("You turn to your left to see a " + adj + " " + noun2 + " " + verb + " towards you.")

        print(name + "! Where are my " + plural + "?!")

        print(name + ", " + verb2 + " out of the way!")

        print("I wouldn't have to " + verb2 + " if I had my " + noun + " and you had your " + plural + "!")

        print("Luckily, you and " + name + " quickly " + verb2 + " out of the way!")

        print("What an eventful day in " + loc + ", and an exhausting one too!")

        print("-------------------------------------------------------------------------------------------------------")

    elif which_lib == "2":

        print("Hey " + name + ", how's it going?")

        print("I could be better, see, my " + noun + " and I went to " + loc + " this weekend.")

        print("The trip was immediately confusing, since my " + noun + " and I are both named " + name + "!")

        print("We had to watch out for a " + adj + " " + noun2 + " and the large group of " + plural + ".")

        print("If the " + noun3 + " and stress wasn't bad enough, I had to " + verb + " to escape the " + plural + ".")

        print("All in all though, being able to " + verb2 + " wasn't so bad though. ")

        print("-------------------------------------------------------------------------------------------------------")

    elif which_lib == "3":

        print("My name is " + name + ". The Superhero of " + loc + " and the defender of " + plural + "!")

        print("My arch-nemesis is The " + adj + " " + noun + "! ")

        print("The streets of " + loc + " will always be safe with me, " + name + "!")

        print("With my amazing " + verb + " and " + verb2 + " abilities, you can sleep safely knowing I am out there!")

        print("I will protect your favorite " + noun + " and " + noun2 + " with the least amount of stress!")

        print("-------------------------------------------------------------------------------------------------------")

    else:
        print("Invalid choice, please try again!")

    loop += 1
