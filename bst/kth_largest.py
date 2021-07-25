# kth largest element in a BST using O(n) extra recursion stack space at worst case
# NOTE: Use Morris traversal algorithm for O(1) extra space constraint. This algorithm doesn't use either stack or recursion in its implementation
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
    
    def kth_largest(self, k, count=0) -> None:
        if not self.left and not self.right:
            count += 1
            if count == k:
                return (count, self.value)
            return (count, None)
        
        if not self.right:
            self.left.kth_largest(k, count)
        
        count, value = self.right.kth_largest(k, count)
        if value: # If value already found from left sub-tree, return that value
            return (count, value)
        count += 1
        if count == k: # If value found from root node, return that value
            return (count, self.value)
        if self.left:
            count, value = self.left.kth_largest(k, count)
        if value: # If value already found from right sub-tree, return that value
            return (count, value)
        return (count, None)

l = Node()
l.insert(10)
l.insert(4)
l.insert(20)
l.insert(2)
l.insert(15)
l.insert(40)
_, value = l.kth_largest(3)
print(value)

