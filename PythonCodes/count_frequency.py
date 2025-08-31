def count_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

numbers = [1, 2, 2, 3, 1, 4, 2]
print(count_frequency(numbers))