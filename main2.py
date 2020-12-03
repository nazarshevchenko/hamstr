import bts, delete

file = open("hamsrt.in.txt", "r").read().split("\n")

for f in range(len(file)):
    file[f] = file[f].split()

S =  int(file[0][0])
C = int(file[1][0])

class Hamsrt:
    def __init__(self, H, G, index):
        self.H = int(H)
        self.G = int(G)
        self.index = int(index)
    def count(self, n):
        return (self.H + (n-1) * self.G)

data = []
for i in range(C):
    x = Hamsrt(int(file[i + 2][0]), int(file[i + 2][1]), i)
    data.append(x)


n = 0
for i in range(C):
    tree = delete.Node(data[0].count(i + 1))
    for j in range(1, C):
        tree.insert(data[j].count(i + 1))
    
    result = tree.print()
    print(result)
    q = 0
    for z in range(i + 1):
        q += result[z]
    
    if q > S:
        break

    else:
        n += 1


print(n)
