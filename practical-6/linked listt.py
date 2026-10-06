class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)

new_node = Node(30)

current = head

while current.next:
    current = current.next

current.next = new_node

current = head

while current:
    print(current.data)
    current = current.next 

