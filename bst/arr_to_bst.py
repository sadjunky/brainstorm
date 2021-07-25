# Convert sorted array to binary search tree 
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
            
        
    
def transform(arr) -> None:
    mid = len(arr) // 2 
    l = Node()
    
    l.insert(arr[mid]) # Make mid point of the array as the root of the tree
     
    for i in range(mid-1, -1, -1):
        l.insert(arr[i])
    
    for i in range(mid+1, len(arr)):
        l.insert(arr[i])
    
    return l

l = transform([1, 2, 3])
l.inorder_traversal()
