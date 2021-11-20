n = int(input())
cnt = [0 for i in range(500001)]
num_list = list(map(int, input().split()))
for i in range(n):
    num = num_list[i]
    cnt[num] += 1
for i in range(len(cnt)-1):
    cnt[i+1] += cnt[i]
for i in num_list:
    print(cnt[i]-1, end = ' ')
#O(n)