def main():
    s = open('input.txt', 'r').read().strip().split(",")
    s = [int(num) for num in s]
    ans = min([sum([(abs(i-num) * (abs(i-num)+1))/2 for num in s]) for i in range(min(s),max(s)+1)])
    print(ans)

main()
