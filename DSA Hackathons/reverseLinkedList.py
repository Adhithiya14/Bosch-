class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

n = int(input().strip())
if n > 0:
    values = list(map(int, input().strip().split()))
    if values:
        head = SinglyLinkedListNode(values[0])
        current = head
        for i in range(1, n):
            current.next = SinglyLinkedListNode(values[i])
            current = current.next
        current = head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("NULL")    
        head = reverse(head)
        current = head
        while current:
            print(current.data, end=" -> ")
            current = current.next
print("NULL")