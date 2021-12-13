def main():
    s = open("input.txt","r").read().split("\n\n")
    s[0] = s[0].splitlines()
    s[0] = [(pair.split(",")[0], pair.split(",")[1]) for pair in s[0]]

    s[1] = s[1].splitlines()
    s[1] = [thing.split()[-1] for thing in s[1]]
    s[1] = [thing.split("=") for thing in s[1]]
    coords = set(s[0])
    instructions = s[1]

    for i in range(len(instructions)):
        c = set()
        for x,y in coords:
            x = int(x)
            y = int(y)
            if instructions[i][0] == 'y':
                y = min(2*int(instructions[i][1])-y,y)
            if instructions[i][0] =='x':
                x = min(2*int(instructions[i][1])-x,x)
            c.add((x,y))
        coords = c

    c = set(c)
    mxX = max(x for x,_ in coords)
    mxY = max(y for _,y in coords)
    grid = [[' '] * (mxX+1) for _ in range(mxY+1)]
    for x,y in coords:
        grid[y][x] = "#"
    print('\n'.join(''.join(row) for row in grid))
main()
