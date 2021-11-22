import sys

def counting_sort(store_list : list, price_list : list):
    cnt = [0 for i in range(1,100001)]
    for i in price_list:
        cnt[i] += 1
    for i in range(len(cnt)-1):
        cnt[i+1] += cnt[i]
    for i in range(len(price_list)):
        store_list[i].append(store_list[i][1]+cnt[price_list[i]])
    return store_list

n = int(sys.stdin.readline())
store_list = []
price_list = []
for i in range(n):
    num,distance,price = map(int, sys.stdin.readline().split())
    store_list.append([num,distance,price])
    price_list.append(price)
store_list = counting_sort(store_list, price_list)
unreasonable_list = sorted(store_list, key=lambda x : (x[3], x[1]))
answer = f'{unreasonable_list[0][0]} {unreasonable_list[0][1]} {unreasonable_list[0][2]}'
print(answer)
#O(n)