from BarcodeReading import *
from InventoryManager import check_inventory_list

def menu():
    while True:
        print("Menu: Read(R), Inventory(I), Exit(E)")
        x = input("Type: ")
        if x.lower() == "read" or x.lower() == "r":
            Read()
        elif x.lower() == "inventory" or x.lower() == "i":
            inventory_menu()
        elif x.lower() == "exit" or x.lower() == "e":
            break
        else:
            print("[ERROR] INCORRECT")

def inventory_menu():
    while True:
        print("Menu: List(L), Add(A), Back(B)")
        x = input("Type: ")
        if x.lower() == "list" or x.lower() == "l":
            check_inventory_list()
        elif x.lower() == "add" or x.lower() == "a":
            print("Add item")
            JAN = input("JAN: ")
            NAME = input("NAME: ")
            PRICE = input("PRICE: ")
            STOCK_QUANTITY = input("STOCK QUANTITY: ")
            add_inventory_item(JAN, NAME, PRICE, STOCK_QUANTITY)
        elif x.lower() == "back" or x.lower() == "b":
            break
        else:
            print("[ERROR] INCORRECT")

if __name__ == "__main__":
    try:
        menu()
        pass
    except KeyboardInterrupt:
        pass