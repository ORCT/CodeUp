def count_down(n):
    if n>0:
        print(n-1)
        count_down(n-1)

count_down(int(input()))