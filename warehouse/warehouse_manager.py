# WAREHOUSE_MANAGER.PY
# ========================
# This is a warehouse management program for a bicycle store.

# Importy
import collections
import csv
import sys
from tabulate import tabulate

# List of Items in the store:
items = [{
    "name": "lights",
    "quantity": 12,
    "unit": "pcs",
    "unit_price": 45.57
    },
    { 
    "name": "breaks",
    "quantity": 30,
    "unit": "pcs",
    "unit_price": 59.99
    },
    { 
    "name": "horn",
    "quantity": 25,
    "unit": "pcs",
    "unit_price": 30.98
    }]


header = {"name":"Name", "quantity":"Quantity", "unit": "Unit", "unit_price":"Unit Price (PLN)"}

add_items = {}

sold_items = []

cost_list = []

income_list = [] 


csv_columns = ["name", "quantity", "unit", "unit_price"]

# Definitions:

def get_items():
    print(tabulate(items, headers= header))

def add_item():
    print("Adding to warehouse...")
    add_name = input("Item name: ")
    for item in items:
        if item["name"] == add_name:
            add_quantity = int(input("Item quantity: "))
            new_quantity = item.get("quantity") + add_quantity
            item.update({"quantity" : new_quantity})
            print("Successfully updated the warehouse. Current status:")
            print(tabulate(items, headers= header))
            return items      
    else:
        add_quantity = int(input("Item quantity: "))
        add_unit = input("Item unit of measure. Eg. l, kg, pcs: ")
        add_price = float(input("Item price in PLN: "))
        add_items = {
            "name" : add_name, 
            "quantity" : add_quantity,
            "unit": add_unit,
            "unit_price" : add_price 
            }
        add_items_copy = add_items.copy()
        items.append(add_items_copy)
        print("Successfully added to warehouse. Current status:")
        print(tabulate(items, headers= header))
        return items

def sell_item():
    print(tabulate(items, headers= header))
    print("Please choose an item from the above list.")
    sell_items = {}
    sell_name = input("Item name: ")
    for item in items:
        if item["name"] == sell_name:
            sell_quantity = int(input("Quantity to sell: "))
            if sell_quantity <= item.get("quantity"):
                new_quantity = item.get("quantity") - sell_quantity
                item.update({"quantity" : new_quantity})
                sell_items.update({
                    "name" : sell_name,
                    "quantity" : sell_quantity,
                    "unit" : item.get("unit"),
                    "unit_price" : item.get("unit_price")
                    })
                sell_items_copy = sell_items.copy()
                sold_items.append(sell_items_copy)
                print(f"Sucessfully sold {sell_quantity} {item.get('unit')} of {sell_name}")
                print(tabulate(items, headers= header))
                return items, sold_items
            else:
                print(f"We don't have that much {sell_name}")

def get_costs():
    for item in items:
        costs = item.get("quantity") *item.get("unit_price")
        cost_list.append(costs)     
    cost_list_sum = sum(cost_list)
    print(f"Costs: {cost_list_sum}")
    return cost_list_sum  

def get_income():
    for item in sold_items:
        income = item.get("quantity") * item.get("unit_price")
        income_list.append(income)     
    income_list_sum = sum(income_list)
    print(f"Income: {income_list_sum}")
    return income_list_sum
    
def show_revenue():
    print("Revenue breakdown (PLN)")
    costs = get_costs()
    income = get_income()
    revenue = f"Revenue:  {income - costs}"
    print("-------------------")
    print(revenue)

def export_items_to_csv(items):
    try:
        with open("magazyn.csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for item in items:
                writer.writerow(item)
    except IOError:
        print("I/O error")

def export_sales_to_csv(sold_items):
    try:
        with open("ewidencja.csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for item in sold_items:
                writer.writerow(item)
    except IOError:
        print("I/O error")

def load_items_from_csv(items):
    try:
        with open("magazyn.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                items.append(row)      
            return items  
    except IOError as err:
            print("I/O error({0})".format(err))    

def load_sold_items_from_csv(sold_items):
    try:
        with open("ewidencja.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sold_items.append(row) 
            return sold_items
    except IOError as err:
            print("I/O error({0})".format(err))    



if __name__ == "__main__":
    
    while True:
        choice = input("What would you like to do? ")
        items = items
        sold_items = sold_items
        if choice == "exit":
            bye = f"Exiting... Bye!"
            print (bye)
            exit()
                
        elif choice =="show":
            get_items()           
            continue

        elif choice == "add":
            add_item()
            continue

        elif choice == "sell":
            sell_item()
            continue    

        elif choice == "show_revenue":
            show_revenue()
            continue    

        elif choice == "save":
            export_items_to_csv(items)
            export_sales_to_csv(sold_items)
            continue    

        elif choice == "load":
            sold_items.clear()
            items.clear()
            load_items_from_csv(items)
            load_sold_items_from_csv(sold_items)
            print(sys.argv)
            print(f"Sucessfully loaded data from magazyn.csv.")
            print(f"Sucessfully loaded data from ewidencja.csv.")
            continue    

        else:
            error = f"Error!"
            print(error)
            exit()