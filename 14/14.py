from collections import Counter
def main():
    s = open("input.txt","r").read().split("\n\n")
    poly = s[0]
    s[1] = s[1].splitlines()
    s[1] = [line.split(" -> ") for line in s[1]]
    rules = {}
    for a,b in s[1]:
        rules[a] = b
    pairs = Counter()
    CC = Counter()
    for i in range(1,len(poly)):
        pairs[poly[i-1]+poly[i]]+=1

    for i in range(len(poly)):
        CC[poly[i]]+=1

    for i in range(40):
        new = Counter()
        for a,b in pairs.items():
            char = rules[a]
            new[a[0]+char] += b
            new[char+a[1]] += b
            CC[char] += b
        pairs = new
    print(max(CC.values()) - min(CC.values()))
main()
