import re
from pathlib import Path
REPORT_PATH = Path(__file__).resolve().parent / "Expense Tracker.txt"
REPORT_PATH.touch(exist_ok=True)

def floatConverter(amount, amountType):
    try:
        fNumber = float(amount)
        amountType = True
        return fNumber, amountType
        
    except:
        print(f'\n"{amount}" is an invalid amount\n')
        return None, amountType
#This makes the program run until the user selects the option that closes it.
expenses = []
running = True
while running == True:
    #This makes a fancy menu pop up and asks for a selection.
    print('\nWhat would you like to do?\n\n===Expense Tracking===\n1-Add a new expense\n2-View all expenses and totals\n3-Save&Exit\n')
    optionSelected = input("Enter your choice (1-3):")
    #If the option is 1, we will ask for the item and the cost of the item.
    if optionSelected == "1":
        itemName = input('What did you purchase?')
        cValid = False
        while cValid == False:
            costInput = input('What was the cost of it?')
            itemCost, cValid = floatConverter(costInput, cValid)
        #This is the confirmation that you are adding the item and makes sure everything looks good.
        confirmation =input(f'\n===Confirming, we are adding "{itemName}" at a price of ${itemCost}?===\nTo confirm this, type "Y" for yes\n')
        if confirmation.lower() == "y":
            itemInfo = {"item": itemName.lower(), "cost": itemCost}
            expenses.append(itemInfo)
            print(f'\n ==={itemName} was added to the report at the price of ${itemCost}===')
    #If option 2 is selected, it we will tally up the total by defaut and print the resualt.
    if optionSelected == '2':
        total = 0
        myExpenses = {}
        with open(REPORT_PATH, "r") as report:
              for line in report:
                   print(line)
                   position = line.find(":")
                   number = float(line[position+1:].strip().strip(")"))
                   total = total + number
        print(f"Your whole report is above\n===The running total for everything in your report is {total}===")
        #This line will ask if you would like to do anything else other than see the running total for everything.
        continueQuestion = input('\nDid you want to do anything else? Type "Y" for yes:')
        #If yes, we create a dictionary and clean up all of the data in the folder so it is easier to work with and then assigns all items to an item key in the dicitonay and the cost will be the value.
        if continueQuestion.lower() == "y":
            lookup = {}
            with open(REPORT_PATH, "r") as report:
                for line in report:                     
                    sLine = line.split()
                    itemLook = sLine[0]
                    itemLook = itemLook.strip("(")
                    costLook = sLine[2]
                    costLook = costLook.strip(")")
                    lookup[itemLook.lower()] = costLook
                #This makes a small little menu that we can add to and will ask questions
                print("\n1-search for an item in the report\nAny other character to exit")
                option = input("What would you like to do?\n")
                #If 1 is entered then it will ask what we are looking for and look up the item and its price with the dictionary.
                if option == "1":
                    askedItem = input(f'What is the item you are looking for?\n')
                    #prints the item and its cost and says if it wasn't found
                    if askedItem.lower() in lookup:
                        print(f'\n==={askedItem} was found with a cost of ${lookup[askedItem.lower()]}===')
                    else:
                        print(f"\n{askedItem} was not found")
    #If option 3 is selected, then all the items that were added on to the list earlier will be added to the text document for use later and then the loop will be broke.               
    if optionSelected == "3":
        with open(REPORT_PATH, "a") as report:
                        for expense in expenses:
                            name = expense["item"]
                            cost = expense["cost"]
                            report.write(f'({name} : {cost})\n')

        print(f'\n===The items you entered were: {expenses}===\n')
        running = False