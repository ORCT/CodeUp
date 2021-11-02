n = int(input(),16)
for i in range(1 , 16):
    answer = n*i
    print(f"{'%X'%n}*{'%X'%i}={'%X'%answer}")