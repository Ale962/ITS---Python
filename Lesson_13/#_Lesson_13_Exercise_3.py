# Lesson Exercise 3

def sumInRange(a, b) -> int:

    sum:int = 0
    
    if b < a:
        
        a_temp = a
        a = b
        b = a_temp

    while b >= a:
        sum += b
        b -= 1

    return sum

print(sumInRange(5, 10))
print(sumInRange(10, 5))