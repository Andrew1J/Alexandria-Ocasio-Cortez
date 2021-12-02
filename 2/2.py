def main():
    nums = open('input.txt', 'r').read().split("\n")[:-1]

    h = 0
    d = 0
    aim = 0

    for i in range(len(nums)):
        stuff = nums[i].split(" ")
        val = int(stuff[1])
        if stuff[0]=='forward':
            h+=val
            d+=(val*aim)
        elif stuff[0]=='down':
            aim+=val
        elif stuff[0]=='up':
            aim-=val
    print(h*d)

if __name__ == "__main__":
    main()
