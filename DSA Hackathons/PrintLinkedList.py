class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLinkedList(head):
    current = head
    while current:
        print(current.data)
        current = current.next

n = int(input())
head = None
tail = None
for _ in range(n):
    data = int(input())
    node = SinglyLinkedListNode(data)
    if not head:
        head = node
        tail = node
    else:
        tail.next = node
        tail = node
print("Linkedlist is:")
printLinkedList(head)
