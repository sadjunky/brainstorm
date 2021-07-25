# Construct a binary search tree from provided inputs and perform deletion of nodes
class Tree:

    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def is_leaf(self):
        return ((self.left is None) and (self.right is None))
    
    def makeempty(self):
        self.value = None
        self.left = None
        self.right = None
    
    def has_one_child(self):
        return ((self.left and not self.right) or (not self.left and self.right))
    
    def insert(self, value) -> str:
        if value == self.value:
            return "Value already inserted"
        
        if value < self.value and self.left:
            self.left.insert(value)
        
        if value > self.value and self.right:
            self.right.insert(value)

        if value < self.value and not self.left:
            self.left = Tree(value)
        
        if value > self.value and not self.right:
            self.right = Tree(value)
    
    def max_val(self): # The rightmost value of the subtree is always the maximum value for a binary search tree
        if self.right:
            return self.right.max_val()
        return self.value
    
    def find(self, value) -> bool:
        if value == self.value:
            return True

        if value < self.value and self.left:
            self.left.find(value)
            return
        
        if value > self.value and self.right:
            self.right.find(value)
            return
        
        return False
    
    def inorder_traversal(self) -> bool:
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
        
    
    def delete(self, value) -> bool:
        if value == self.value:
            if self.is_leaf():
                self.makeempty()
                return True
            
            if self.has_one_child():
                if self.left:
                    self.value = self.left.value
                    left = self.left.left
                    right = self.left.right
                    self.left = left
                    self.right = right
                else:
                    self.value = self.right.value
                    left = self.right.left
                    right = self.right.right
                    self.left = left
                    self.right = right
                return True
            
            self.value = self.left.max_val()
            self.left.delete(self.value) # Remove the maximum element from its former position
            return True

        if value < self.value and self.left:
            return self.left.delete(value)
        
        if value > self.value and self.right:
            return self.right.delete(value)
        
        return False

t = Tree(52)
t.insert(37)
t.insert(74)
t.insert(16)
t.insert(44)
t.insert(28)
t.insert(21)
t.insert(74)
t.insert(91)
t.insert(83)
t.delete(52)
t.inorder_traversal()
