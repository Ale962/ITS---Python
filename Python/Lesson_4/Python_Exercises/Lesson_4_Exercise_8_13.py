# Lesson 4 exercise 8.13

'''
8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
'''

def build_profile(name: str, surname: str, age: int, nationality: str, hair: str) -> None:

    print(f"{name} {surname}, age: {age}, nationality: {nationality}, hair-color; {hair}")


build_profile("Alessio", "Caico", 29, "Italian", "dark blonde")