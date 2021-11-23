n,m = map(int, input().split())
board = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    board.append([name,score])
board.sort(key = lambda x : -x[1])
for i in range(m):
    print(board[i][0])
#O(n)