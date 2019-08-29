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
        input_item = user_input("Input item: ")
        create(input_item)
    # Read item
    elif function_code == "R":
        length = len(checklist)
        # Remember that item_index must actually exist or our program will crash.
        while True:
            input_index = user_input("Index Number(0-" + str(length-1) + ")? ")
            if input_index < length and input_index >= 0:
                read(item_index)
                break
            print "You have made an invalid choice, try again."
    # Print all items
    elif function_code == "P":
        list_all_items()
    # Catch all
    else:
        print("Unknow Option")

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    # mark_completed(0)
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))

    select("C")

    list_all_items()

    select("R")

    list_all_items()

test()
