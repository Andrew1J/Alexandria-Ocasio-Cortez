from collections import deque

def main():
    s = open("input.txt","r").read().splitlines()
    s = [[str(num) for num in line] for line in s]
    match = { ")":"(", "]":"[", "}":"{", ">":"<" }
    match2 = { "(":")", "[":"]", "{":"}", "<":">" }
    values = { ")" : 1, "]" : 2, "}" : 3, ">" : 4 }

    ans = []
    for line in s:
        queue = deque()
        noncorrupted = True
        for squiggle in line:
            if squiggle not in match.keys():
                queue.append(squiggle)
            else:
                beg = queue.pop()
                if beg != match[squiggle]:
                    noncorrupted = False
        if noncorrupted:
            queue.reverse()
            curr = 0
            for num in queue:
                curr = (5*curr) + values[match2[num]]
            ans.append(curr)
    ans.sort()
    print(int(len(ans)/2))
    print(ans[int(len(ans)/2)])



main()
