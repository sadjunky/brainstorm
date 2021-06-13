# zigzag tree traversal
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def zigzag(root):
    deque = []
    deque.insert(0, root)
    level = 0 
    print(root.data, end =" ")
    while deque:
        size = len(deque)
        for i in range(size): # Breadth wise iteration of nodes for every tree level
            if level % 2 == 0:
                parent = deque.pop(0)
                if parent.right:
                    deque.append(parent.right)
                    print(parent.right.data, end=" ")
                if parent.left:
                    deque.append(parent.left)
                    print(parent.left.data, end=" ")
            else:
                parent = deque.pop()
                if parent.left:
                    deque.insert(0, parent.left)
                    print(parent.left.data, end=" ")
                if parent.right:
                    deque.insert(0, parent.right)
                    print(parent.right.data, end=" ")
        level += 1 # Increment to next tree level

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)

zigzag(root)
