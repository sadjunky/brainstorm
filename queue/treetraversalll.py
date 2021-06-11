# Breadth first tree traversal using linked list
class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:

    def __init__(self):
        self.root = None
        self.head = None

    def push(self, data):
        if not self.root:
            self.root = self.head = Node(data)
            return
        if not self.root.left:
            self.root.left = Node(data)
            return
        if not self.root.right:
            self.root.right = Node(data)
            self.root = self.root.left
            return

    def traverse(self):
        queue = []
        queue.insert(0, self.head)
        while queue:
            parent = queue.pop()
            print(parent.data, end=" ")
            if parent.left:
                queue.insert(0, parent.left)
            if parent.right:
                queue.insert(0, parent.right)
    

t = Tree()
t.push(1)
t.push(2)
t.push(3)
t.push(4)
t.push(5)
t.traverse()
