def sum_kwargs(**kwargs):
    return sum(kwargs.values())

print(sum_kwargs(a=1, b=2, c=3))