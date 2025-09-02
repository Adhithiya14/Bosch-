class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peek from empty stack")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Dequeue from empty queue")
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Peek from empty queue")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = BSTNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node is not None and node.value == value
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)
    
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def preorder(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self._hash(key)
        for item in self.buckets[index]:
            if item[0] == key:
                item[1] = value
                return
        self.buckets[index].append([key, value])
    
    def get(self, key):
        index = self._hash(key)
        for item in self.buckets[index]:
            if item[0] == key:
                return item[1]
        raise KeyError("Key not found")
    
    def remove(self, key):
        index = self._hash(key)
        for i, item in enumerate(self.buckets[index]):
            if item[0] == key:
                self.buckets[index].pop(i)
                return
        raise KeyError("Key not found")

def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print("Stack size:", stack.size())
    print("Stack peek:", stack.peek())
    print("Stack pop:", stack.pop())
    print("Stack is empty:", stack.is_empty())
    
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print("Queue size:", queue.size())
    print("Queue peek:", queue.peek())
    print("Queue dequeue:", queue.dequeue())
    print("Queue is empty:", queue.is_empty())
    
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.prepend(0)
    print("Linked List:")
    ll.display()
    ll.delete(1)
    print("After delete:")
    ll.display()
    
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    print("BST Inorder:", bst.inorder())
    print("BST Preorder:", bst.preorder())
    print("BST Postorder:", bst.postorder())
    print("BST Search 3:", bst.search(3))
    print("BST Search 10:", bst.search(10))
    
    hm = HashMap()
    hm.put("name", "Alice")
    hm.put("age", 30)
    print("HashMap get name:", hm.get("name"))
    hm.remove("name")
    try:
        print(hm.get("name"))
    except KeyError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()