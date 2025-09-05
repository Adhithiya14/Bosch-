def getMax(operations):
    stack = []
    max_values = []
    
    for op in operations:
        if op[0] == '1':  
            num = int(op.split()[1])
            stack.append(num)
        elif op[0] == '2':  
            if stack:
                stack.pop()
        elif op[0] == '3': 
            if stack:
                max_values.append(max(stack))
    
    return max_values
    
n = int(input())

operations = []
for _ in range(n):
    operations.append(input().strip())


results = getMax(operations)

for result in results:
    print(result)






