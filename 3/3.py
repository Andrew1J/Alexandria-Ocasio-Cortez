def main():
    s = open('input.txt', 'r').read().splitlines()
    s2 = s

    g=0
    e=0

    for i in range(len(s[0])):
        cntone=0
        new_s=[]
        for j in range(len(s)):
            if s[j][i]=='1':
                cntone+=1
        if cntone>=len(s)/2:
            for j in range(len(s)):
                if(s[j][i]=='1'):
                    new_s.append(s[j])
        else:
            for j in range(len(s)):
                if(s[j][i]=='0'):
                    new_s.append(s[j])

        s=new_s
        if len(new_s)==1:
            break

    for i in range(len(new_s[0])):
        if(new_s[0][i]=='1'):
            e += pow(2,len(new_s[0])-1-i)

    for i in range(len(s2[0])):
        cntone=0
        new_s=[]
        for j in range(len(s2)):
            if s2[j][i]=='1':
                cntone+=1
        if cntone>=len(s2)/2:
            for j in range(len(s2)):
                if(s2[j][i]=='0'):
                    new_s.append(s2[j])
        else:
            for j in range(len(s2)):
                if(s2[j][i]=='1'):
                    new_s.append(s2[j])

        s2=new_s
        if len(new_s)==1:
            break

    for i in range(len(new_s[0])):
        if(new_s[0][i]=='1'):
            g += pow(2,len(new_s[0])-1-i)

    print(e*g)

if __name__ == "__main__":
    main()
