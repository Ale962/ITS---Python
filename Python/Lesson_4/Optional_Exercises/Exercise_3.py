# Optional Exercise 3

'''
3. E-commerce Shopping Cart:

    Create a function that defines a product with a name, price, and quantity.
    Create functions that manage the shopping cart, allowing the user to add, remove, and view products in the cart.
    Create a function that calculates the cart total and apply any discounts or taxes.
    Create a funciton to print a detailed summary of the cart including products and totals.
    Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.

'''

def Product(name: str, price: float, quantity: int) -> dict[str, dict[str, str|float|int]]:

    return {"Name": name, "Price": price, "Quantity": quantity}

def ProductInput() -> dict:
    name = input("Write the product name here: ")
    price = float(input("Write the price of the product here: "))
    quantity = int(input("Write the quantity of the product here: "))
    product: dict = {name: {"Name": name, "Price": price, "Quantity": quantity}}
    return product


def Summary(cart: dict[str, dict[str, str|float|int]]) -> None:
    if not cart:
        print("The Shopping Cart is empty, please add a product to see a summary of the shopping cart")
    print("The Shopping Cart is: ")
    for k, v in cart.items():
        print(f"\nProduct: {k}")
        print(f"Price: {v['Price']}")
        print(f"Quantity: {v['Quantity']}")

def ShoppingCart() -> dict[str, dict[str, str|int|float]]:

    shopping_cart: dict = {}

    while True:

        request = input("Do you want to add, remove a product or do you want a summary of the shopping cart? (a: add a product, r: remove a product, s: summary, q: to quit the programm): ")

        if request.lower() == "a":
            name = input("Write the product name here: ")
            price = float(input("Write the price of the product here: "))
            quantity = int(input("Write the quantity of the product here: "))
            shopping_cart[name] = (Product(name, price, quantity))

        elif request.lower() == "r":
            product_to_remove = input("Write the product that you want to remove here: ").lower()
            products_list = {k.lower(): k for k in shopping_cart}
            if product_to_remove in products_list:
                del shopping_cart[products_list[product_to_remove]]
            else:
                print("Coldn't find the product inserted")

        elif request.lower() == "s":
            Summary(shopping_cart)

        elif request.lower() == "q":
            break

    return shopping_cart

def Total(sc: dict[str, dict[str, str|float|int]]) -> float:

    total: float = 0
    
    for p in sc.values():
        total += (p["Price"]*p["Quantity"])

    tax = input("There are any taxes to apply? (Y or N): ")
    if tax.upper() == "Y":
        tax_value = float(input("Insert the tax to apply: "))
        tax_to_apply = (total/100) * tax_value
        total += tax_to_apply
    else:
        pass

    discount = input("There is any discount to apply? (Y or N): ")
    if discount.upper() == "Y":
        discount_value = float(input("Insert the discount value: "))
        discount_to_apply = (total/100) * discount_value
        total -= discount_to_apply

    return total

def DetailedSummary(sc: dict[str, dict[str, str|float|int]]) -> None:
    Summary(sc)
    print(Total(sc))

if __name__ == "__main__":

    cart = {
    "Laptop": {"Name": "Laptop", "Price": 1000.0, "Quantity": 1},
    "Mouse": {"Name": "Mouse", "Price": 50.0, "Quantity": 2},
    "Keyboard": {"Name": "Keyboard", "Price": 80.0, "Quantity": 1}
    }

    DetailedSummary(cart)
    ShoppingCart()