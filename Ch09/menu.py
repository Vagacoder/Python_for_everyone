##
#  This module defines the Menu class.
#

## A menu that is displayed in the terminal window.
#
class Menu :
   ## Constructs a menu with no options.
   #
   def __init__(self) :
      self._options = ''
      self._optionNumber = 0
   
   ## Adds an option to the end of this menu.
   #  @param option the option to add
   #
   def addOption(self, option) :
      self._options += option 
      self._options += '\n'
      self._optionNumber += 1
   
   ## Displays the menu, with options numbered starting with 1, and prompts
   #  the user for input. Repeats until a valid input is supplied.
   #  @return the number that the user supplied
   #
   def getInput(self) :
      menuItems = self._options.split('\n')
      done = False
      while not done :
         for i in range(self._optionNumber) :
            print("%d %s" % (i + 1, menuItems[i].strip()))
    
         userChoice = int(input())
         if userChoice >= 1 and userChoice < len(self._options) :
            done = True
           
      return userChoice
