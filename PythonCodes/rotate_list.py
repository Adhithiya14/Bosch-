def rotate_list(lst, k):
    if not lst:
        return lst
    k = k % len(lst)
    return lst[k:] + lst[:k]

numbers = [1, 2, 3, 4, 5]
k = 2
print(rotate_list(numbers, k))