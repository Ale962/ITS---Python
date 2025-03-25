import time
# Recursive Fuction Introduction

def countdown (n:int) -> None:

    if n < 0:                                               # Stopping case (if n is a negative number)
        print("Error, the number inserted is negative")

    elif n == 0:                                            # Stopping case
        print(0)

    else:
        print(n)
        time.sleep(1)
        countdown(n-1)

countdown(-5)
countdown(5)