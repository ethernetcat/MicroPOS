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