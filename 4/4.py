def main():
    s = open('input.txt', 'r').read().strip().splitlines()
    draws = s[0].split(',')
    grid = []

    for i in range(len(s)):
        if i!=0 and s[i]!="":
            n = s[i].split()
            n = [int(num) for num in n]
            grid.append(n)

    w = set()

    for draw in draws:
        for i in range(0,len(grid)-4,5):
            grid = mark(grid,int(draw), i)
            if win(grid, i):
                w.add(i)
            if len(w) == int((len(grid))/5):
                print(int(draw)*sum(grid,i))
                return

def mark(grid,draw, i):
    for row in range(5):
        for col in range(5):
            if grid[row+i][col] == draw:
                grid[row+i][col] = -1
    return grid

def win(grid,i):
    for j in range(5):
        wincol = True
        winrow = True
        for k in range(5):
            if grid[j+i][k] != -1:
                wincol = False
            if grid[k+i][j] != -1:
                winrow = False
        if wincol or winrow:
            return True
    return False

def sum(grid,i):
    for j in range(5):
        wincol = True
        winrow = True
        for k in range(5):
            if grid[j+i][k] != -1:
                wincol = False
            if grid[k+i][j] != -1:
                winrow = False
        if wincol or winrow:
            sum=0
            for j in range(5):
                for k in range(5):
                    if grid[j+i][k] != -1:
                        sum+=grid[j+i][k]
            return sum
    return -1

main()
