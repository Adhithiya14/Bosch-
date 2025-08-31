def find_min_max(lst):
    if not lst:
        return None, None
    smallest = largest = lst[0]
    for num in lst[1:]:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return smallest, largest

numbers = [3, 1, 4, 1, 5, 9, 2]
min_num, max_num = find_min_max(numbers)
print(f"Smallest: {min_num}, Largest: {max_num}")