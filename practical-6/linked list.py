class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

# Connect nodes
n1.next = n2
n2.next = n3

# Display linked list
current = n1

while current:
    print(current.data)
    current = current.next
