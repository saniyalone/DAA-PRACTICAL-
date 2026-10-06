class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(20)
head.next = Node(30)

# Insert new node
new_node = Node(10)
new_node.next = head
head = new_node

# Display
current = head

while current:
    print(current.data)
    current = current.next
