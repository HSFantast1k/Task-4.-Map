N, M = map(int, input().split())
map = [[int(j) for j in input().split()] for i in range(N)]
square_count = 0 #Переменная для подсчета кол-чи квадратов


def check(i, j):
    global square_count
    # print("Next колонка")
    Flag_right = True
    right_count = 0
    while Flag_right:
        right = map[i][j + right_count]
        if right == 0:
            # print(f"ряд - {i}, колонка - {j} right_count {right_count - 1}")
            Flag_right = False
        else:
            right_count += 1

    Flag_bottom = True
    bottom_count = 0
    while Flag_bottom:
        bottom = map[i + bottom_count][j]
        if bottom == 0:
            # print(f"ряд - {i}, колонка - {j} bottom_count {bottom_count - 1}")
            Flag_bottom = False
        else:
            map[i + bottom_count][j] = 0
            map[i + bottom_count][j + right_count - 1] = 0
            bottom_count += 1

    # print(f"Размеры ширина {right_count} Длина {bottom_count}")
    if right_count == bottom_count:
        square_count += 1
        # print("Квадрат")
    #for row in map:
    #    for elem in row:
    #        print(elem, end=' ')
    #    print()

for i in range(N):
    for j in range(M):
        if map[i][j] == 1:
            check(i, j)

print(square_count)