def find_disappeared_numbers(nums: list) -> list[int]:
    
    disappeared_numbers: list[int]= []

    for x in range(1, len(nums) + 1):
        if x in nums:
            continue
        else:
            disappeared_numbers.append(x)
            
    disappeared_numbers_sorted: list = sorted(disappeared_numbers)
    
    print(disappeared_numbers_sorted)
    
    return disappeared_numbers_sorted



numbers: list[int] = [1, 3, 5, 6, 7, 2, 1]
find_disappeared_numbers(numbers)