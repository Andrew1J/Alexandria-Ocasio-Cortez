from queue import PriorityQueue

s = open("input.txt","r").read().splitlines()
s = [[int(num) for num in line] for line in s]

visited = set()

def dijkstras(s):
    pq = PriorityQueue()
    pq.put((0, (0, 0)))
    visited = {(0,0)}
    while pq:
        dist,(x,y) = pq.get()

        if (x==len(s)-1 and y==len(s[0])-1):
            return dist

        for i,j in [[-1,0],[1,0],[0,-1],[0,1]]:
            if not outofbounds(s,x+i,y+j) and (x+i,y+j) not in visited:
                weight = s[x+i][y+j]
                pq.put((dist + weight, (x+i, y+j)))
                visited.add((x+i,y+j))

def outofbounds(graph,i,j):
    return (i>=len(graph) or j>=len(graph[0]) or i<0 or j<0)

def biggify():
    r, c = len(s) * 5, len(s[0]) * 5
    big = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            cur = (s[i % len(s)][j % len(s[0])] + i // len(s) + j // len(s[0]))
            if cur != 9:
                cur %= 9
            big[i][j] = cur
    return big


print(biggify())
print(dijkstras(biggify()))
