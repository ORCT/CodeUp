n = int(input())
call = list(map(int, input().split()))
check = []
for i in range(1,24):
    check.append(call.count(i))
for i in check:
    print(i,end = ' ')