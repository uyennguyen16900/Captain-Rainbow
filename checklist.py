#For more information about adding colors to texts, I read from https://pypi.org/project/termcolor/
import sys
from termcolor import colored

checklist = list()

# CREATE
def create(item):
    checklist.append(item)
# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        # print("%S %S" % (index, list_item))
        index += 1

def mark_completed(index):
    item = checklist[index]
    if item[0] == "√":
        print(colored("You already marked this item.", "red"))
        input = user_input(colored("Do you want to unmark it? Y/N ", "red"))
        if input.upper() == "Y":
            checklist[index] = item[1:]
    else:
        checklist[index] = "√" + item

def select(function_code):
    # Create list_item
    if function_code.upper() == "A":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif function_code.upper() == "R":
        length = len(checklist)
        # if key R is pressed when the list is empty
        if length == 0:
            print(colored("No items to read.", "red"))
        # runs when there is(are) item(s) in the list
        else:
            while True:
                item_index = user_input("Index Number(0-" + str(length-1) + ")? ")
                if int(item_index) < length and int(item_index) >= 0:
                    print(read(int(item_index)))
                    break
                print(colored("You have made an invalid choice, try again.", "red"))

    #remove
    elif function_code.upper() == "E":
        length = len(checklist)
        if length == 0:
            print(colored("No items to remove.", "red"))
        else:
            while True:
                item_index = user_input("Which item to cancel(0-" + str(length-1) + ")? (X to cancel) ")
                if item_index.upper() == "X":
                    break
                elif int(item_index) < length and int(item_index) >= 0:
                    destroy(int(item_index))
                    break
                print(colored("You have made an invalid choice, try again.", "red"))

    # Print all items
    elif function_code.upper() == "P":
        if len(checklist) == 0:
            print(colored("No items to display.", "red"))
        else:
            list_all_items()

    # update
    elif function_code.upper() == "U":
        length = len(checklist)
        if length == 0:
            print(colored("No items to upate.", "red"))
        else:
            while True:
                item_index = user_input("Index Number(0-" + str(length-1) + ")? ")
                if int(item_index) < length and int(item_index) >= 0:
                    item = user_input("Update it to: ")
                    update(int(item_index), item)
                    break
                print(colored("You have made an invalid choice, try again.", "red"))

    # Mark completed
    elif function_code.upper() == "M":
        length = len(checklist)
        if length == 0:
            print(colored("No items.", "red"))
        else:
            while True:
                item_index = user_input("Which item to mark as completed(0-" + str(length-1) + ")? ")
                if int(item_index) < length and int(item_index) >= 0:
                    mark_completed(int(item_index))
                    break
                print(colored("You have made an invalid choice, try again.", "red"))

    # Catch all
    elif function_code.upper() == "Q":
        return False
    else:
        print("Unknow Option")
    return True

def user_input(prompt):
    user_input = input(prompt)
    return user_input

#TEST
def test():
    # create("purple sox")
    # create("red cloak")
    #
    # print(read(0))
    # # mark_completed(0)
    # print(read(1))
    #
    # update(0, "purple socks")
    #
    # destroy(1)
    #
    # print(read(0))

    # select(selection)

    list_all_items()

    # select(selec)

    # list_all_items()
    # name = user_input("Enter name: ")
    # print(name)
test()

running = True
while running:
    selection = user_input(colored(
        "Press A to add to list, R to read from list, E to remove, P to display list, U to update, M to mark as completed (press again to unmark), and Q to quit: ", "blue"))
    running = select(selection)
