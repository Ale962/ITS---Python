# Lesson 3 Exercise 6.3

'''
6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
'''


glossary: dict = {"append": "Append is used to add at the end of a list an element", "pop": "Pop is used to eliminate an element from a list", "extend": "Extend is used to extend the list with an element", "sort": "Sort is used to sort a list", "reverse": "Reverse invert the order of a list"}

for key, value in glossary.items():
    print (f'\n{key}\n\n{value}')