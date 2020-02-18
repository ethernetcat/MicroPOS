import csv

def get_items_csv():
    with open("items.csv", encoding="utf_8") as file:
        items = list(csv.reader(file))
    return items

def get_purchased_csv():
    with open("purchased.csv", encoding="utf_8") as file:
        purchaced = list(csv.reader(file))
    return purchaced