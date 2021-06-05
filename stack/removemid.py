
class Stack:
    
    def __init__(self):
        self.items = []
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()
    
    def display(self):
        print(self.items)
    
    def empty(self):
        return self.top == None
    
    def size(self):
        return len(self.items)

def delete_mid(s, n, cur):
    if cur == int(n/2):
        s.pop()
    else:
        temp = s.pop()
        delete_mid(s, n, cur+1)
        s.push(temp)
    


if __name__=='__main__':
	
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
	
    print("Original Stack")
    s.display()
	
	# Reverse
    delete_mid(s, s.size(), 0)

    print("Modified Stack")
    s.display()
