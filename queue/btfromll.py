# Conversion of linked list to its equivalent binary tree
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __children(self, parent, index):
        index_left = (2*index)+1
        temp = parent
        while index != index_left and temp is not None:
            temp = temp.next
            index += 1
        return (temp, temp.next if temp else None)
    
    def __list_traverse(self, parent, root):
        temp = root
        index = 0
        while temp:
            if temp.data == parent.data:
                return self.__children(temp, index)
            temp = temp.next
            index += 1
        
    def inorder_traversal(self, parent):
        if not parent.left:
            print(parent.data, end=" ")
            return
        self.inorder_traversal(parent.left) 
        print(parent.data, end=" ")
        if parent.right: self.inorder_traversal(parent.right)

    def construct(self, root):
        queue = []
        queue.insert(0, self)
        while queue:
            parent = queue.pop()
            (c1, c2) = self.__list_traverse(parent, root)
            parent.left = c1
            parent.right = c2
            if c1: queue.insert(0, c1)
            if c2: queue.insert(0, c2)


root = Node(10)
root.next = Node(12)
root.next.next = Node(15)
root.next.next.next = Node(25)
root.next.next.next.next = Node(30)
root.next.next.next.next.next = Node(36)

t = Tree(root.data)
t.construct(root)
t.inorder_traversal(t)
