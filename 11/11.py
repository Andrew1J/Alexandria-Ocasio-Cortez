s = open("input.txt","r").read().splitlines()
s = [[int(num) for num in line] for line in s]

def main():
    ans = 0
    for _ in range(100000):
        for i in range(len(s)):
            for j in range(len(s[0])):
                s[i][j]+=1
        for i in range(len(s)):
            for j in range(len(s[0])):
                if s[i][j]>9:
                    ans += flash(i,j)
        good = True
        for i in range(len(s)):
            for j in range(len(s[0])):
                if s[i][j]==-1:
                    s[i][j]=0
                else:
                    good = False

        if good:
            print("Part2: " + str(_+1))
            break
        if _ == 99:
            print("Part1: " + str(ans))

def flash(i, j):
    ans = 1
    s[i][j] = -1
    for dx,dy in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
        if inbounds(i+dx,j+dy) and s[i+dx][j+dy]!=-1:
            s[i+dx][j+dy] += 1
            if s[i+dx][j+dy]>9:
                ans += flash(i+dx,j+dy)
    return ans

def inbounds(i,j):
    return not (i>=len(s) or j>=len(s[0]) or i<0 or j<0)

main()
