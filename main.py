def check(i, j):
    print("Next колонка")
    cout = 0
    while cout != 1:
        # Flag = True
        # top_count = 1
        # while Flag:
        #     top = map[i - top_count][j]
        #     if top == 0:
        #         print(f"ряд - {i}, колонка - {j} top_count {top_count - 1}")
        #         Flag = False
        #     else:
        #         top_count += 1
        Flag_bottom = True
        bottom_count = 0
        while Flag_bottom:
            bottom = map[i + bottom_count][j]
            if bottom == 0:
                print(f"ряд - {i}, колонка - {j} bottom_count {bottom_count - 1}")
                Flag_bottom = False
            else:
                bottom_count += 1
        Flag_right = True
        right_count = 0
        while Flag_right:
            right = map[i][j + right_count]
            if right == 0:
                print(f"ряд - {i}, колонка - {j} right_count {right_count - 1}")
                Flag_right = False
            else:
                right_count += 1
        cout += 1


N, M = map(int, input().split())
processed_column = []
map = [[int(j) for j in input().split()] for i in range(N)]
for i in range(N):
    for j in range(M):
        if map[i][j] == 1:
            check(i, j)
    print()