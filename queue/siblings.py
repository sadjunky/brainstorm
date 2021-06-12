# Compute siblings of a tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.child = []
    
def siblings(root, x):
    queue = []
    queue.insert(0, root)
    while queue:
        parent = queue.pop()
        for child in parent.child:
            if child.data == x:
                return len(parent.child) - 1
        for child in parent.child:
            queue.insert(0, child)
    return 0

root = Node(50) 
(root.child).append(Node(2)) 
(root.child).append(Node(30)) 
(root.child).append(Node(14)) 
(root.child).append(Node(60)) 
(root.child[0].child).append(Node(15)) 
(root.child[0].child).append(Node(25)) 
(root.child[0].child[1].child).append(Node(70)) 
(root.child[0].child[1].child).append(Node(100)) 
(root.child[1].child).append(Node(6)) 
(root.child[1].child).append(Node(1)) 
(root.child[2].child).append(Node(7)) 
(root.child[2].child[0].child).append(Node(17)) 
(root.child[2].child[0].child).append(Node(99)) 
(root.child[2].child[0].child).append(Node(27)) 
(root.child[3].child).append(Node(16))

print(siblings(root, 100))
