from InventoryManager import *

def Read(item_list):
    Read_list = []
    SUM = 0

    print("Read ready.")
    while True:
        i = 0
        barcode = input()
        if barcode != "":
            Read_list.append(barcode)
            for i in range(len(item_list)):
                if barcode == item_list[i][0]:
                    print("# 商品名", item_list[i][1], "価格", round(int(item_list[i][2])*1.10), "（", round(int(item_list[i][2])*0.10), "）")
        else:
            break
        i += 1

    for i in range(len(Read_list)):
        for j in range(len(item_list)):
            if Read_list[i] == item_list[j][0]:
                print("商品名", item_list[j][1], "価格", round(int(item_list[j][2])*1.10), "（", round(int(item_list[j][2])*0.10), "）")
                SUM += round(int(item_list[j][2])*1.10)

    print("####################")
    print("合計金額", str(SUM))
    print("####################")

    update_inventory(Read_list, item_list)