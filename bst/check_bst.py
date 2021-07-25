from typing import List


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
    
    def check_bst(self) -> None:
        if not self.left and not self.right:
            return self.value # Return value of traversed node
        if not self.left:
            self.right.check_bst()
        
        prev = self.left.check_bst() # Return value will be used for comparing with current node
        if not prev:
            return False
        if prev > self.value:
            return False
        if self.right:
            prev = self.right.check_bst()
        if not prev:
            return False
        if prev < self.value:
            return False
        return prev

l = Node(4)
l.left = Node(2)
l.right = Node(5)
l.left.left = Node(1)
l.left.right = Node(3)
if l.check_bst():
    print(True)
else:
    print(False)
