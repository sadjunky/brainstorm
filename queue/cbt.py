# Check whether Binary Tree is a Complete Binary Tree
class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def iscbt(root):
    queue = []
    queue.insert(0, root)
    incomplete = 0
    while queue:
        parent = queue.pop()
        if (parent.left or parent.right) and (incomplete > 0):
            return False
        if (not parent.left) and parent.right:
            return False
        if parent.left and (not parent.right):
            incomplete += 1 
        if not parent.left and not parent.right:
            incomplete += 1
        if parent.left: queue.insert(0, parent.left)
        if parent.right: queue.insert(0, parent.right)
    return True

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

if (iscbt(root)):
    print("Complete Binary Tree")
else:
    print("NOT Complete Binary Tree")
