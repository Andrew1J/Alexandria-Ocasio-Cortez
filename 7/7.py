
print(min([sum([(abs(i-num) * (abs(i-num)+1))/2 for num in [int(num) for num in [int(num) for num in open('input.txt', 'r').read().strip().split(",")]]]) for i in range(min([int(num) for num in [int(num) for num in open('input.txt', 'r').read().strip().split(",")]]),max([int(num) for num in [int(num) for num in open('input.txt', 'r').read().strip().split(",")]])+1)]))
