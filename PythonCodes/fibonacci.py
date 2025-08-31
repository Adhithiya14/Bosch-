def fibonacci(num: int) -> int:
    if num < 0:
        print("Incorrect input")
        return
    elif num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(9))