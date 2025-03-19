# Lesson 13 Recursive SumInRange

def recursiveSumInRange(a:int, b:int) -> int:
    
    # if a > b, swap values of a and b
    if a > b:                                           
        temp:int = a                                    # define a temporary variable called temp, containing value of a
        a = b                                           # swap values of a and b
        b = temp                                        # now b = a
    
    if b == a:                                          # otherwise, compute the sum recursively
        return int(a)
    
    else:                                               # otherwise, compute the sum recursively
        return int(b + recursiveSumInRange(a, b-1))
    
print(recursiveSumInRange(5, 10))
print(recursiveSumInRange(10, 5))