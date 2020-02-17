from Read import get_items_csv, get_purchased_csv

def check_purchased_history():
    Items_list = get_items_csv()
    Purchased_history = get_purchased_csv()
    for i in range(len(Purchased_history)):
        print(Purchased_history[i])