# Lowest Common Ancestor (LCA) of two nodes in a BST
class Node:

    def __init__(self, value=None) -> None:
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value) -> None:
        if not self.value:
            self.value = value
            return
        if value < self.value and self.left:
            self.left.insert(value)
        if value > self.value and self.right:
            self.right.insert(value)
        if value < self.value and not self.left:
            self.left = Node(value)
        if value > self.value and not self.right:
            self.right = Node(value)
    
    def lca(self, n1, n2) -> None:
        if self.value > n1 and self.value > n2:
            return self.left.lca(n1, n2)
        if self.value < n1 and self.value < n2:
            return self.right.lca(n1, n2)
        else:
            return self.value

l = Node()
l.insert(20)
l.insert(8)
l.insert(22)
l.insert(4)
l.insert(12)
l.insert(10)
l.insert(14)

print(l.lca(10, 22))
