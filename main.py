def check(i, j):
    print("Next колонка")
    Flag_bottom = True
    bottom_count = 0
    while Flag_bottom:
        bottom = map[i + bottom_count][j]
        if bottom == 0:
            print(f"ряд - {i}, колонка - {j} bottom_count {bottom_count - 1}")
            processed_ranks.append(i + (bottom_count - 1)) # Запись обработаных рядов с j до j + (right_count - 1) есть какой-то дом
            Flag_bottom = False
        else:
            bottom_count += 1
    Flag_right = True
    right_count = 0
    while Flag_right:
        right = map[i][j + right_count]
        if right == 0:
            print(f"ряд - {i}, колонка - {j} right_count {right_count - 1}")
            processed_column.append(j + (right_count - 1))  #Запись обработаных колонок с j до j + (right_count - 1) есть какой-то дом
            Flag_right = False
        else:
            right_count += 1
    print(processed_column)
    print(processed_ranks)

N, M = map(int, input().split())
processed_column = [] #Колонки которые не нужно обрабатовать
processed_ranks = [] #Ряды которые не нужно обрабатовать
map = [[int(j) for j in input().split()] for i in range(N)]
for i in range(N):
    for j in range(M):
        if map[i][j] == 1:
            check(i, j)
    print()
