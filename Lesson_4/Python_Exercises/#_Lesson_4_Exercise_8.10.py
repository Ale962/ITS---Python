# Lesson 4 Exercise 8.10

'''
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.
''' 

salutations: list = ["Hello!", "Saludad!", "Ciao!", "Salut!", "Halo!", "Hola!"]
sent_massage: list = []

def send_message(list, list2):
    for x in list:
        print(x)
        list2.append(x)
    list.clear()

send_message(salutations, sent_massage)

print(sent_massage)
print(salutations)