

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if data < self.data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        
        elif data >= self.data:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)
    
    def print(self):
        result = []
        if self.left:
            result += self.left.print()
        
        result.append(self.data)

        if self.right:
            result += self.right.print()
        
        return result