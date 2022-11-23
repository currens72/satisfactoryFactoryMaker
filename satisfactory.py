import itemList

def itemCreation():
    print("Select the item you wish to make from the list here https://satisfactory.fandom.com/wiki/Category:Items")
    item = input("Type in the item you wish to create (not case sensitive): ")
    amount = input("Desired output per minute: ")
    amount = int(amount)
    item = item.lower()
    itemList.itemSelection(item, amount)

def menu():
    print("---------------------------------------------")
    print("Enter 1 to select ore you wish to start with.")
    print("Enter 2 to select item you wish to make.")
    print("Enter 3 to exit.")
    print("---------------------------------------------")
    x = input("Selection: ")
    print()
    x = int(x)
    if x == 1:
        print(x)
    elif x == 2:
        itemCreation()
    elif x == 3:
        print()
        print("Goodbye, you should play more satisfactory though.")
        exit()
    else:
        print(">>INVALID SELECTION")
        menu()

def main():
    menu()

main()
