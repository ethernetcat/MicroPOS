from Update import *

def update_inventory(Read_list, item_list):
    for i in range(len(Read_list)):
        for j in range(len(item_list)):
            if Read_list[i] == item_list[j][0]:
                item_list[j][3] = int(item_list[j][3])-1
    update_items_csv(item_list)
    update_purchaced_csv(Read_list)