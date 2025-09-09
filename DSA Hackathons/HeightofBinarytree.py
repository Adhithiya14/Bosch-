class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if not root:
        return -1
    left = height(root.left)
    right = height(root.right)
    return max(left, right) + 1

n = int(input().strip())
if n > 0:
    values = list(map(int, input().strip().split()))
    if values:
        root = Node(values[0])
        queue = [root]
        i = 1
        while queue and i < len(values):
            node = queue.pop(0)
            if i < len(values) and values[i] != -1:
                node.left = Node(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] != -1:
                node.right = Node(values[i])
                queue.append(node.right)
            i += 1
        print(height(root))