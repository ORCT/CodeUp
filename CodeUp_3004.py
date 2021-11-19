#n = int(input())
#num_list = list(map(int, input().split()))
#sorted_num_list = sorted(num_list)
#number_sequence = []
#for i in range(n):
#    for j in range(n):
#        if sorted_num_list[j] == num_list[i]:
#            number_sequence.append(j)
#for i in range(n):
#    print(number_sequence[i], end = ' ')
n = int(input())
num_list = list(map(int, input().split()))
cnt_list = [0 for i in range(500001)]
for i in num_list:
    cnt_list[i] += 1
for i in range(len(cnt_list)):
    for j in range(cnt_list[i]):
        print(i)