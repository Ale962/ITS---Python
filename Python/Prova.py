def nums_evens(nums: list[int]) -> int:
    sum: int = 0
    nums_evens: list[int] = [x for x in nums if x % 2 == 0]
    for x in nums_evens:
        sum += x

    return sum