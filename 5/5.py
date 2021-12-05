def main():
    s = open('input.txt', 'r').read().splitlines()
    s = [line.split() for line in s]
    for line in s:
        line.pop(1)
    mx = findmax(s)
    arr = [[0]*(mx+1) for i in range(mx+1)]

    for line in s:
        x1 = int(line[0].split(',')[0])
        y1 = int(line[0].split(',')[1])
        x2 = int(line[1].split(',')[0])
        y2 = int(line[1].split(',')[1])
        if x1 == x2 or y1 == y2 or abs(x1-x2) == abs(y2-y1):
            arr = drawvent(arr,x1,y1,x2,y2)
            
    cnt = 0
    for i in range(mx+1):
        for j in range(mx+1):
            if arr[i][j]>=2:
                cnt+=1
    print(cnt)

def findmax(s):
    mx = 0
    for line in s:
        mx = max(int(line[0].split(',')[0]),int(line[0].split(',')[1]),mx)
        mx = max(int(line[1].split(',')[0]),int(line[1].split(',')[1]),mx)
    return mx

def drawvent(arr,x1,y1,x2,y2):
    if x1==x2:
        # 2 4, 2 1
        for i in range(min(y1,y2),max(y1,y2)+1):
            arr[i][x1]+=1
        return arr
    elif y1==y2:
        for j in range(min(x1,x2),max(x1,x2)+1):
            arr[y1][j]+=1
        return arr
    elif abs(x1-x2) == abs(y1-y2):
        if x1 < x2 and y1 < y2:
            for i in range(x1,x2+1):
                arr[y1+(i-x1)][i]+=1
            return arr
        elif x1 < x2 and y1 > y2:
            for i in range(x1,x2+1):
                arr[y1-(i-x1)][i]+=1
            return arr
        elif x2 < x1 and y2 > y1:
            for i in range(x2,x1+1):
                arr[y2-(i-x2)][i]+=1
            return arr
        elif x2 < x1 and y2 < y1:
            for i in range(x2,x1+1):
                arr[y2+(i-x2)][i]+=1
            return arr
main()
