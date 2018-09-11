# This module defines the menu class

class Menu:
    # Constructs a menu with no options
    def __init__(self):
        self._options = []

    def addOption(self,option):
        self._options.append(option)

    # Displays the menu, with options numbered string with 1,
    # And prompts the user for input.
    # Repeats until a valid input is supplied

    def getInput(self):
        done = False
        while not done:
            for i in range(len(self._options)):
                print("%d %s" %(i + 1, self._options[i]))

            userChoice = int(input("Enter a Value: "))
            if userChoice >= 1 and userChoice < len(self._options):
                    done = True
        return userChoice

