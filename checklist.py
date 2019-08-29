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

#NOT FINISHED mark_completed


def select(function_code):
    # Create list_item
    if function_code == "C":
        input_item = raw_input("Input item: ")
        create(input_item)
    # Read item
    elif function_code == "R":
        length = len(checklist)
        while True:
            item_index = raw_input("Index Number(0-" + str(length-1) + ")? ")
            if int(item_index) < length and int(item_index) >= 0:
                read(int(item_index))
                break
            print "You have made an invalid choice, try again."
    # Print all items
    elif function_code == "P":
        list_all_items()
    # Catch all
    elif function_code == "Q":
        return False
    else:
        print("Unknow Option")
    return True

def user_input(prompt):
    user_input = raw_input(prompt)
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
        "Press C to add to list, R to Read from list, P to display list, and Q to quit: ")
    running = select(selection)
