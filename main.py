from UpdateCSV import *

Read_list = []
SUM = 0

item_list = get_items_csv()

print("Read ready:")
while True:
    i = 0
    barcode = input()
    if barcode != "":
        Read_list.append(barcode)
    else:
        break
    i += 1

for i in range(len(Read_list)):
    for j in range(len(item_list)):
        if Read_list[i] == item_list[j][0]:
            print("商品名", item_list[j][1], "価格", round(int(item_list[j][2])*1.10), "（", round(int(item_list[j][2])*0.10), "）")
            SUM += round(int(item_list[j][2])*1.10)

print("合計金額", str(SUM))

for i in range(len(Read_list)):
    for j in range(len(item_list)):
        if Read_list[i] == item_list[j][0]:
            item_list[j][3] = int(item_list[j][3])-1

update_items_csv(item_list)
update_purchaced_csv(Read_list)