# Lesson 3 Exercise 4.15

'''4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.'''

# From Exercise 4.2

pizzas: list[str] = ["Margherita", "4 Formaggi", "Boscaiola", "Diavola"]        # implemention of PEP8 type-in

for a in pizzas:
    print(a)
    print(f"I really like pizza {a}")


print(f"Pizza is my favorite food because i love to eat it.\nIn particular I love pizza {pizzas[3]}\nIt is my personal favourite")