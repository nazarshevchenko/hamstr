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

def Insert(sort, n):
    for i in range(1, len(sort)):

        number = sort[i]

        for j in range(i - 1, -1, -1):
            if number.count(n) >= sort[j].count(n):
                break
            
            sort[j + 1] = sort[j]
            sort[j] = number
    return sort

data = []
for i in range(C):
    x = Hamsrt(int(file[i + 2][0]), int(file[i + 2][1]), i)
    data.append(x)

sorted = []
n = 0
for i in range(C):
    sorted = Insert(data, i + 1)
    count = 0
    for j in range(i+1):
        count += sorted[j].count(i + 1)

    if count > S:
        break
    else:
        n += 1
    

file = open("hamsrt.out.txt", "w").write(str(n))
print(n)