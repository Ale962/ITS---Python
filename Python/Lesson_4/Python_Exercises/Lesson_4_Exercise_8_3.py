# Lesson 4 Exercise 8.3

'''
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
'''

def make_shirt(size:str, message:str):
    print(f"The siza of the shirt is {size} and the message to print on it is {message}")

sizes: list[str] = ["XXS", "XS", "S", "M","L", "XL", "XXL", "XXXL"]

while True:

    size: str = input("Write the size of the t-shirt here (XXS/XS/S/M/L/XL/XXL/XXXL): ")    

    if size in sizes:
        break

message: str = input("Write the message you want on your t-shirt here: ")

make_shirt(size, message)