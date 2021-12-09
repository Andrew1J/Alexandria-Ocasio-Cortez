def main():
    s = open("input.txt","r").read().splitlines()
    s = [[int(num) for num in line] for line in s]
    visited = [[0]*len(s[0]) for _ in range(len(s))]

    low_points = []
    for x in range(len(s)):
        for y in range(len(s[0])):
            is_low = True
            for i,j in [[-1,0],[1,0],[0,-1],[0,1]]:
                if outofbounds(s,x+i,y+j):
                    continue;
                else:
                    if s[x+i][y+j] <= s[x][y]:
                        is_low = False
            if is_low:
                low_points.append((x,y))

    ans = []
    for x,y in low_points:
        ans.append(dfs(s,visited,x,y))
    ans.sort(reverse=True)
    print(ans[0]*ans[1]*ans[2])


def outofbounds(map,i,j):
    return (i>=len(map) or j>=len(map[0]) or i<0 or j<0)


def dfs(map, visited, x, y):
    if map[x][y] == 9 or visited[x][y]:
        return 0
    else:
        cnt = 1
        visited[x][y] = 1
        for i,j in [[-1,0],[1,0],[0,-1],[0,1]]:
            if not outofbounds(map,x+i,y+j):
                cnt += dfs(map,visited,x+i,y+j)
    return cnt

main()
