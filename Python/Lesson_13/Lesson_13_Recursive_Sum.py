# Lesson 13 Recursive Sum

def recursiveSum(n:int) -> int:

    if n < 0:                                           # stopping case n is negative
        print("Error! Inserted number is negative!")
        return None
    
    elif n == 0:                                        # stopping case when n reach 0
        return 0
    
    else:
        return int(n + recursiveSum(n-1))
    
print(recursiveSum(-5))
print(recursiveSum(5))