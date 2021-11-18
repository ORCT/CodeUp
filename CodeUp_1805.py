n = int(input())
number = []
gas = []
for i in range(n):
    a,b = map(int, input().split())
    number.append(a)
    gas.append(b)
sorted_number = sorted(number)
for i in sorted_number:
    for j in range(len(number)):
        if i==number[j]: 
            print(i,gas[j])