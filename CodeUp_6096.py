board = []
for i in range(19):
    line = list(map(int, input().split()))
    board.append(line)
n = int(input())
for i in range(n):
    r,c = map(int, input().split())
    for j in range(19):
        if board[r-1][j] == 0: board[r-1][j] = 1
        else: board[r-1][j] = 0
    for k in range(19):
        if board[k][c-1] == 0: board[k][c-1] = 1
        else: board[k][c-1] = 0
for i in range(19):
    for j in range(19):
        print(board[i][j], end = ' ')
    print()