# Lesson 13 Exercise 2

# first method

def sum(n) -> int:

    sum = 0

    if n < 0:
        print("Error, the number inserted is negative")
        return None

    while True:

        if n >= 0:
            sum += n
            n -= 1

        else:
            break
    
    return(sum)

print(sum(-5))
print(sum(5))