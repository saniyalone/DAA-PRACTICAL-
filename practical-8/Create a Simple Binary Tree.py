class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(10)

root.left = Node(20)
root.right = Node(30)

print("Root:", root.data)
print("Left:", root.left.data)
print("Right:", root.right.data)

