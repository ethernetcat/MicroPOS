import csv

def get_items_csv():
    with open("items.csv", encoding="utf_8") as file:
        items = list(csv.reader(file))
    return items