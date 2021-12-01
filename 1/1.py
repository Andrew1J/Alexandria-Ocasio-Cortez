def main():
    nums = open('input.txt', 'r').read().split("\n")[:-1]
    nums = [int(i) for i in nums]

    cnt = 0

    # Part 1
    # for i in range(len(nums)-1):
    #     if nums[i] < nums[i+1]:
    #         cnt+=1

    # Part 2
    for i in range(len(nums)-3):
        if nums[i]+nums[i+1]+nums[i+2] < nums[i+1]+nums[i+2]+nums[i+3]:
            cnt+=1

    print(cnt)

if __name__ == "__main__":
    main()
