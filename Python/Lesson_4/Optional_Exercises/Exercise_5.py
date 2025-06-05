# Optional Exercise 5

'''
5. Inventory Management System:

    Create a list to store the items in inventory.
    Create a function that defines an item with a code, name, quantity, and price.
    Implement functions to add, remove, search, and update items in the inventory.
    Use for loops to manage the various inventory operations.

'''
inventory: list[dict[str, str|int|float]] = []

def item(code: str, name: str, quantity: int, price: float) -> dict:
    return {"code": code, "name": name, "quantity": quantity, "price": price}

def add_item(l: list[dict[str, str|int|float]]) -> None:
    code: str = input("Insert the code of the item: ")
    name: str = input("Insert the name of the item: ")
    quantity: int = int(input("Insert the quantity of the item: "))
    price: float = float(input("Insert the price of the item: "))
    i = item(code, name, quantity, price)
    present = search_item(l, i.get("name"))
    if present:
        print("Item alreay in the list")
        question = input("Do you want to update the item? (Y or N): ")
        if question.upper() == "Y":
            update_item(l, i.get("name"))
        else:
            pass
    else:    
        l.append(i)
        print("Item successfuly added")

def remove_item(l: list[dict[str, str|int|float]], name: str) -> None:
    # lambda solution
    # l = list(filter(lambda d: d.get("name") != name, l))
    # return l
    found = False
    for d in l:
        if name in d.get("name"):
            l.remove(d)
            found = True
            print("Item removed")
            break
    if not found:
        print("Item not found")

def search_item(l: list[dict[str, str|int|float]], name: str) -> dict|None:
    for d in l:
        if name in d.get("name"):
            print("Item found")
            return d
    print("Item not present in the inventory")

def update_item(l: list[dict[str, str|int|float]], name: str) -> None:
    i = search_item(l, name)
    if i:
        i["quantity"] = int(input("Insert the quantity of the item: "))
        i["price"] = float(input("Insert the price of the item: "))
        print("Item updated")

def inventory_management(l: list[dict[str, str|int|float]]):
    
    answer = input("What do you want to do? Insert a to add an item, r to remove an item, s to search for an item, u to update an existing item: ")
    match answer.lower():
        case "a":
            add_item(l)
        case "r":
            name: str = input("Insert the name of the item: ")
            remove_item(l, name)
        case "s":
            name: str = input("Insert the name of the item: ")
            search_item(l, name)
        case "u":
            name: str = input("Insert the name of the item: ")
            update_item(l, name)
        case _:
            pass