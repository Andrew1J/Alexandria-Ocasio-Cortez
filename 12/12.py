def main():
    s = open("input.txt","r").read().splitlines()
    paths = {}
    for line in s:
        a, b = line.split("-")
        if a not in paths:
            paths[a] = []
        if b not in paths:
            paths[b] = []
        paths[a].append(b)
        paths[b].append(a)
    print(dfs(paths, ["start"]))

def dfs(paths, path):
    ans = 0
    curr = path[-1]
    if curr == 'end':
        ans+=1
        return ans
    for thing in paths[curr]:
        if thing=='start':
            continue
        if not thing.islower() or thing not in path or canaddlower(path):
            ans += dfs(paths, path+[thing])

    return ans

def canaddlower(path):
    c = [p for p in path if p.islower()]
    s = set()
    for cave in c:
        s.add(cave)
    return (abs(len(c) - len(s)) < 1)

main()
