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

#NOT FINISHED
def mark_completed(index):
    item = checklist[index]
    if item[0] == "√":
        print("You already marked this item.")
        input = user_input("Do you want to unmark it? Y/N ")
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
        while True:
            item_index = user_input("Index Number(0-" + str(length-1) + ")? ")
            if int(item_index) < length and int(item_index) >= 0:
                print(read(int(item_index)))
                break
            print("You have made an invalid choice, try again.")

    #remove
    elif function_code.upper() == "E":
        length = len(checklist)
        while True:
            item_index = user_input("Which item to cancel(0-" + str(length-1) + "? (X to cancel) ")
            if item_index.upper() == "X":
                break
            elif int(item_index) < length and int(item_index) >= 0:
                destroy(int(item_index))
                break
            print("You have made an invalid choice, try again.")


    # Print all items
    elif function_code.upper() == "P":
        list_all_items()

    # update
    elif function_code.upper() == "U":
        length = len(checklist)
        while True:
            item_index = user_input("Index Number(0-" + str(length-1) + ")? ")
            item = user_input("Update it to: ")
            if int(item_index) < length and int(item_index) >= 0:
                update(int(item_index), item)
                break
            print("You have made an invalid choice, try again.")


    # Mark completed
    elif function_code.upper() == "M":
        length = len(checklist)
        while True:
            item_index = user_input("Which item to mark as completed(0-" + str(length-1) + ")? ")
            if int(item_index) < length and int(item_index) >= 0:
                mark_completed(int(item_index))
                break
            print("You have made an invalid choice, try again.")

    # Catch all
    elif function_code.upper() == "Q":
        return False
    else:
        print("Unknow Option")
    return True

def user_input(prompt):
    user_input = input(prompt)
    return user_input


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
    selection = user_input(
        "Press A to add to list, R to read from list, E to remove, P to display list, U to update, M to mark as completed (press again to unmark), and Q to quit: ")
    running = select(selection)
