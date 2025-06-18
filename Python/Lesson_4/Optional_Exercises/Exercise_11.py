# Exercise 11

'''
11. Sieve of Eratosthenes Prime Number Generator:

    Create a function that generates a list of prime numbers up to a specified limit using the Sieve of Eratosthenes algorithm.
    Initialize an array of all numbers up to the limit, marking each number as prime initially.
    Iterate through the array, starting from 2, and mark every multiple of the current number as non-prime.
    The remaining unmarked numbers are the prime numbers within the limit.
    Return the list of prime numbers.

'''

def PrimeNumberGenerator(limit: int) -> list[int]:

    numbers: dict[int, bool] = {}
    for n in range(2, limit+1):
        numbers[n] = True

    for i in range(2, int(limit**0.5)+1):
        if numbers[i] == True:
            j = i**2
            while j <= limit:
                numbers[j] = False
                j += i
    
    prime_numbers: list[int] = []

    for key, value in numbers.items():
        if value == True:
            prime_numbers.append(key)

    return prime_numbers

if __name__ == '__main__':
   print(PrimeNumberGenerator(100))