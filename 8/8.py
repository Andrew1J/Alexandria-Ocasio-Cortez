def main():
    s = open("input.txt","r").read().splitlines()
    s = [line.split("|") for line in s]
    digits = {}
    ans = 0
    for i in range(len(s)):
        digits = {}
        digits2 = {}
        nums = s[i][0].split()
        decode = s[i][1].split()

        while len(digits)<10:
            for num in nums:
                sorted_chars = sorted(num)
                newstr = "".join(sorted_chars)

                # 1 7 4 8
                if len(num) == 2:
                    digits[1] = newstr
                    digits2[newstr] = 1
                elif len(num) == 3:
                    digits[7] = newstr
                    digits2[newstr] = 7
                elif len(num) == 4:
                    digits[4] = newstr
                    digits2[newstr] = 4
                elif len(num) == 7:
                    digits[8] = newstr
                    digits2[newstr] = 8

                # 2 3 5
                if len(num) == 5:
                    # 3
                    if 1 in digits.keys() and countmissing(digits[1],newstr)==0:
                        digits[3] = newstr
                        digits2[newstr] = 3
                    # 2
                    if 4 in digits.keys() and countmissing(newstr, digits[4])==3:
                        digits[2] = newstr
                        digits2[newstr] = 2
                    # 5
                    if 4 in digits.keys() and 1 in digits.keys() and countmissing(digits[1],newstr)==1 and countmissing(newstr,digits[4])==2:
                        digits[5] = newstr
                        digits2[newstr] = 5

                # 0 6 9
                if len(num) == 6:
                    # 9
                    if 4 in digits.keys() and countmissing(digits[4],newstr)==0:
                        digits[9] = newstr
                        digits2[newstr] = 9
                    # 6
                    if 1 in digits.keys() and 4 in digits.keys() and countmissing(digits[4], newstr)==1 and countmissing(digits[1],newstr)==1:
                        digits[6] = newstr
                        digits2[newstr] = 6
                    # 0
                    if 1 in digits.keys() and 4 in digits.keys() and countmissing(digits[4], newstr)==1 and countmissing(digits[1],newstr)==0:
                        digits[0] = newstr
                        digits2[newstr] = 0


        thing = ""
        for num in decode:
            sorted_chars = sorted(num)
            newstr = "".join(sorted_chars)
            thing += str(digits2[newstr])
        ans += int(thing)
    print(ans)

def countmissing(str1,str2):
    countmissing = 0
    for c in str1:
        if c not in str2:
            countmissing +=1
    return countmissing
main()
