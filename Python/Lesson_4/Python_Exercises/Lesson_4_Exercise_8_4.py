# Lesson 4 Exercise 8.4

'''
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
'''

def make_shirt(size:str, message:str):
    print(f"The siza of the shirt is {size} and the message to print on it is {message}")

size1 = "L"
message1 = "I Love Python"

make_shirt(size1, message1)

size2 = "M"

make_shirt(size2, message1)

sizes: list[str] = ["XXS", "XS", "S", "M","L", "XL", "XXL", "XXXL"]

while True:

    size: str = input("Write the size of the t-shirt here (XXS/XS/S/M/L/XL/XXL/XXXL): ")    

    if size in sizes:
        break
    else: 
        print("Size not avaible")


message: str = input("Write the message you want on your t-shirt here: ")

make_shirt(size, message)