from InventoryManager import *
from Read import get_items_csv

def Read():
    Read_list = []
    Item_list = get_items_csv()
    SUM = 0

    print("Read ready.")
    while True:
        i = 0
        barcode = input()
        if barcode != "":
            Read_list.append(barcode)
            for i in range(len(Item_list)):
                if barcode == Item_list[i][0]:
                    print("NAME: {0}, PRICE: {1}(In-TAX:{2})".format(Item_list[i][1], round(int(Item_list[i][2])*1.10), round(int(Item_list[i][2])*0.10)))
        else:
            break
        i += 1

    for i in range(len(Read_list)):
        for j in range(len(Item_list)):
            if Read_list[i] == Item_list[j][0]:
                SUM += round(int(Item_list[j][2])*1.10)

    print("####################")
    print("合計金額", str(SUM))
    print("####################")

    update_inventory(Read_list)