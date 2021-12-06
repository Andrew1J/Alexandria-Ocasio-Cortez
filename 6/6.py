def part1():
    s = open('input.txt', 'r').read().strip().split(',')
    s = [int(fish) for fish in s]
    s=[0]
    for i in range(256):
        for i in range(len(s)):
            if s[i] > 0:
                s[i] -= 1
            elif s[i] == 0:
                s[i] = 6
                s.append(8)
                continue;
    print(len(s))

def part2():
    s = open('input.txt', 'r').read().strip().split(',')
    s = [int(fish) for fish in s]
    cnt = [s.count(i) for i in range(9)]
    print(cnt)
    for i in range(256):
        cntzero = cnt[0]
        for i in range(8):
            cnt[i] = cnt[i+1]
        cnt[6] += cntzero
        cnt[8] = cntzero
    print(sum(cnt))
    
def main():
    part2()

main()
