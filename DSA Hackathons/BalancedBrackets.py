def isBalanced(s):
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
        elif c in ")]}":
            if not stack:
                return "NO"
            top = stack.pop()
            if (c == ")" and top != "(") or (c == "]" and top != "[") or (c == "}" and top != "{"):
                return "NO"
    return "YES" if not stack else "NO"

n = int(input())
for _ in range(n):
    s = input().strip()
    print(isBalanced(s))