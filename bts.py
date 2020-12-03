


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def insert(self, data):
        if self.data <= data:
            if self.right == None: 
                self.right = Node(data)
            else:
                self.right.insert(data)
        
        elif self.data > data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        
    def print(self):
        result = []
        if self.left:
            some = self.left.print()
            result += some
        result.append(self.data)

        if self.right:
            some = self.right.print()
            result += some
        
        return result

'''
a = Node(5)
a.insert(6)
a.insert(0)
a.insert(9)
a.insert(4)
a.insert(11)
print(a.print())
'''