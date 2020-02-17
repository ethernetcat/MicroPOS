from BarcodeReading import *
from InventoryManager import check_inventory_list

def menu():
    while True:
        print("Menu: Read(R), Inventory(I), Exit(E)")
        x = input("Type: ")
        if x == "Read" or x == "R":
            Read()
        elif x == "Inventory" or x == "I":
            inventory_menu()
        elif x == "Exit" or x == "E":
            break
        else:
            print("[ERROR] INCORRECT")

def inventory_menu():
    while True:
        print("Menu: List(L), Add(A), Back(B)")
        x = input("Type: ")
        if x == "List" or x == "L":
            check_inventory_list()
        elif x == "Add" or x == "A":
            print("Add item")
            JAN = input("JAN: ")
            NAME = input("NAME: ")
            PRICE = input("PRICE: ")
            STOCK_QUANTITY = input("STOCK QUANTITY: ")
            add_inventory_item(JAN, NAME, PRICE, STOCK_QUANTITY)
        elif x == "Back" or x == "B":
            break
        else:
            print("[ERROR] INCORRECT")

if __name__ == "__main__":
    try:
        menu()
        pass
    except KeyboardInterrupt:
        pass