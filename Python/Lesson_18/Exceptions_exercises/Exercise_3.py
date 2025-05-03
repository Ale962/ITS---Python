# Lesson 18 Exercise 3

'''
Context Managers for File Handling: Use the with statement and context managers to open and close a file. Handle potential IOError within the with block for clean resource management.

'''

def OpenFile(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
            return text
    except IOError:
        return "Could Not Open the file"