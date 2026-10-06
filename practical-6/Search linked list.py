class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

search = int(input("Enter value to search: "))

current = head
found = False

while current:
    if current.data == search:
        found = True
        break
    current = current.next

if found:
    print("Element found")
else:
    print("Element not found")
