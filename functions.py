import time
def loadList(file_name_local):
    with open(file_name_local) as f:
        list_local = f.read().splitlines()

    return list_local


def printList(the_list, list_title=""):
    print(list_title)
    if len(the_list) == 0:
        print("\nNo items in list")
    for index, item in enumerate(the_list):
        list_index = int(index)
        print(f"{list_index + 1}. {item}")

def addItem(the_list, the_item):
    if len(the_item) > 0:
        the_list.append(the_item)
    return the_list


def editItem(the_list_local):
    # printList(the_list, "\nTODO:")
    if len(the_list_local) == 0:
        return the_list_local

    list_num = int
    try:
        list_num = int(input("Enter number of item to edit or 0 to exit: ")) - 1
    except ValueError:
        print("Invalid entry. Try again.")
        editItem(the_list_local)

    if list_num < 0:
        # this is if they enter 0 to exit
        return the_list_local
    elif list_num + 1 > len(the_list_local):
        print("\nInvalid number. Try again.")
        editItem(the_list_local)
    elif list_num >= 0:
        print("Old value: ", the_list_local[list_num])
        the_list_local[list_num] = input("Enter the new value: ")


def deleteItem(the_list_local):
    # printList(the_list_local, "\nTODO:")
    if len(the_list_local) == 0:
        return the_list_local

    # Make sure they didn't enter a string
    list_num = int
    try:
        list_num = int(input("Enter number of the item to delete or 0 to exit: ")) - 1
    except ValueError:
        print("Invalid entry. Try again.")
        deleteItem(the_list_local)

    # This is to exit the function if they enter 0
    if list_num < 0:
        pass

    elif list_num + 1 > len(the_list_local):
        print("Invalid number. Try again.")
        deleteItem(the_list_local)

    elif list_num >= 0:
        print(f'"{the_list_local[list_num]}" has been removed')
        the_list_local.pop(list_num)

    return the_list_local
def updateFileList(file_name_local, list_local):
    print(f"Updating {file_name_local}")
    file_list = []
    for item_local in list_local:
        # file_list.append(item_local)
        file_list.append(item_local + "\n")

    with open(file_name_local, "w") as file_local:
        date = time.strftime("%b %d, %Y %H:%M:%S %p")
        print("writing to file", date)
        file_local.writelines(file_list)
