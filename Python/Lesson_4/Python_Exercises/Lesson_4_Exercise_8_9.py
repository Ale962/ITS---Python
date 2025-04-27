# Lesson 4 Exercise 8.9

'''
8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.
'''

salutations: list = ["Hello!", "Saludad!", "Ciao!", "Salut!", "Halo!", "Hola!"]

def send_message(list):
    for x in list:
        print(x)

send_message(salutations)