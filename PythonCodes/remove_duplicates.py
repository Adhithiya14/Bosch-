def remove_duplicates(lst):
    result = []
    seen = set()
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

numbers = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(numbers))