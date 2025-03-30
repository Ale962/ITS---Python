# Exercise Lesson 13

def countdown(a):

    if a < 0:
        print("Error, number inseted is a negative number")

    while True:

        if a >= 0:
            print(a)
            a -= 1

        else:
            break

countdown(-5)
countdown(5)