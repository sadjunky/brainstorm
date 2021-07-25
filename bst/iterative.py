# Iterative inorder traversal of binary tree
class Node:

    def __init__(self, value=None) -> None:
        self.value = value
        self.left = None
        self.right = None
    
    def inorder_traversal(self) -> None:
        stack = []
        if not self.left and not self.right:
            print(self.value, end=" ")
            return
        current = self
        while True:
            if current:
                stack.append(current)
                current = current.left
            
            # Backtrack from the empty subtree and visit the Node
            # at the top of the stack; however, if the stack is
            # empty you are done
            elif stack:
                current = stack.pop()
                print(current.value, end=" ")
                current = current.right
            else: break

l = Node(1)
l.left = Node(2)
l.left.left = Node(4)
l.left.right = Node(5)
l.right = Node(3)

l.inorder_traversal()
