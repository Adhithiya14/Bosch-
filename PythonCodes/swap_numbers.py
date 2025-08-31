def swap_numbers(a, b):
    print(f"Before swap: a = {a}, b = {b}")
    a = a + b
    b = a - b
    a = a - b
    print(f"After swap: a = {a}, b = {b}")
    return a, b

swap_numbers(5, 10)