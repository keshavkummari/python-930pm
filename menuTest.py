# This program tests the Menu Class

from menu import Menu

mainMenu = Menu()

mainMenu.addOption("Open new account")
mainMenu.addOption("Log into existing account")
mainMenu.addOption("Help")
mainMenu.addOption("Quit")

choice = mainMenu.getInput()

print("Input: ", choice)
