# Breadth first tree traversal using list
class Tree:

    def __init__(self):
        self.tree = []
    
    def push(self, node):
        self.tree.append(node)
    
    def __children(self, parent):
        try:
            left = self.tree[2*self.tree.index(parent)+1]
        except:
            left = None
        try:
            right = self.tree[2*self.tree.index(parent)+2]
        except:
            right = None
        return (left, right)
        
    def traverse(self):
        queue = []
        queue.insert(0, self.tree[0])
        while queue:
            parent = queue.pop()
            print(parent, end=" ")
            for children in self.__children(parent):
                if children:
                    queue.insert(0, children)

t = Tree()
t.push(1)
t.push(2)
t.push(3)
t.push(4)
t.push(5)
t.traverse()
