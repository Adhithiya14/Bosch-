def second_largest(lst):
    if len(lst) < 2:
        return None
    largest = second = float('-inf')
    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second if second != float('-inf') else None

numbers = [10, 5, 8, 12, 3]
print(second_largest(numbers))