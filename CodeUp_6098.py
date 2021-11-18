maze = []
for i in range(10):
    maze.append(list(map(int, input().split())))
x,y = 1,1
maze[x][y] = 9
while 1:
    if maze[x][y+1] == 1:
        if maze[x+1][y] == 0:
            x += 1
            maze[x][y] = 9
        elif maze[x+1][y] == 1:
            maze[x][y] = 9
            break
        else:
            x += 1
            maze[x][y] = 9
            break
    elif maze[x][y+1] == 0:
        y += 1
        maze[x][y] = 9
    else:
        y += 1
        maze[x][y] = 9
        break
for i in range(10):
    for j in range(10):
        print(maze[i][j], end =' ')
    print()