X = 5
A = [1, 3, 1, 4, 2, 3, 5, 4]
river_pos = [False] * (X+1)
print("this is river_pos", river_pos)
print(A)
for i in range(len(A)):
    pos = A[i]
    print(pos)
    if not river_pos[pos]:
        river_pos[pos] = True
        print("this is updated river_pos", river_pos)
        X -= 1
        if X == 0:
            print("this is the time", i)
        else:
            print(-1)
