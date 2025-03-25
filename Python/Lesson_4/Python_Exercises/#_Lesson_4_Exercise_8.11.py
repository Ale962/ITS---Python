# Lesson 4 exercise 8.11

'''
8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.
'''

salutations: list = ["Hello!", "Saludad!", "Ciao!", "Salut!", "Halo!", "Hola!"]
sent_massage: list = []

def send_message(list, list2):
    for x in list:
        print(x)
        list2.append(x)

send_message(salutations, sent_massage)

print(sent_massage)
print(salutations)