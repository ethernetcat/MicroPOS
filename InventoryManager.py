from Update import *
from Read import get_items_csv

def update_inventory(Read_list):
    Item_list = get_items_csv()
    for i in range(len(Read_list)):
        for j in range(len(Item_list)):
            if Read_list[i] == Item_list[j][0]:
                Item_list[j][3] = int(Item_list[j][3])-1
    update_items_csv(Item_list)
    update_purchaced_csv(Read_list)

def check_inventory_list():
    Item_list = get_items_csv()
    for i in range(len(Item_list)):
        print("JAN: {0:<13}, Price: {1}, Remaining: {2}".format(Item_list[i][0], Item_list[i][2], Item_list[i][3]))
