import csv

def update_items_csv(array):
    with open("items.csv", "w", encoding="utf_8") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerows(array)

def update_purchaced_csv(array):
    with open("purchaced.csv", "a", encoding="utf_8") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(array)