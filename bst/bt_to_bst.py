# Convert binary tree to binary search tree 
# NOTE: This algorithm uses O(n) space where n is the number of nodes in the binary tree
class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
    
    def store_traversal(self, arr) -> None:
        if not self.left and not self.right:
            arr.append(self.value)
            return arr
        
        if not self.left:
            arr.append(self.value)
            self.right.store_traversal(arr)
            return arr
        
        self.left.store_traversal(arr)
        arr.append(self.value)
        if self.right:
            self.right.store_traversal(arr)
        
        return arr
    
    def traverse_and_replace(self, arr) -> None:
        if not self.left and not self.right:
            if self.value: self.value = arr.pop(0)
            return
        
        if not self.left:
            if self.value: self.value = arr.pop(0)
            self.right.traverse_and_replace(arr)
            return
        
        self.left.traverse_and_replace(arr)
        
        if self.value: self.value = arr.pop(0)
        
        if not self.right:
            return
        self.right.traverse_and_replace(arr)
    
    def inorder_traversal(self) -> None:
        if not self.left and not self.right:
            if self.value: print(self.value, end=" ")
            return
        
        if not self.left:
            if self.value: print(self.value, end=" ")
            self.right.inorder_traversal()
            return
        
        self.left.inorder_traversal()
        
        if self.value: print(self.value, end=" ")
        
        if not self.right:
            return
        self.right.inorder_traversal()
    
    def transform(self) -> None:
        arr = self.store_traversal([])
        arr.sort()
        self.traverse_and_replace(arr)


l = Node(10)
l.left = Node(30)
l.right = Node(15)
l.left.left = Node(20)
l.right.right = Node(5)
l.transform()
l.inorder_traversal()
