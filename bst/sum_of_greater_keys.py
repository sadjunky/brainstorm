# Convert a BST to a Binary Tree such that sum of all greater keys is added to every key
class Node:

    def __init__(self, value=None) -> None:
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
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
    
    def reverse_inorder_traversal(self, sum=0) -> None: # Reverse inorder traversal to sum all the values and store them subsequently
        if not self.left and not self.right:
            sum += self.value
            self.value = sum
            return sum
        
        if not self.right:
            sum += self.value
            self.value = sum
            return self.left.reverse_inorder_traversal(sum)
        
        sum = self.right.reverse_inorder_traversal(sum)
        
        sum += self.value
        self.value = sum

        if self.left:
            sum = self.left.reverse_inorder_traversal(sum)
        
        return sum
    
    def transform(self) -> None:
        self.reverse_inorder_traversal()

l = Node()
l.insert(5)
l.insert(2)
l.insert(13)
l.transform()
l.inorder_traversal()

