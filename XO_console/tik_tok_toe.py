def win_checker(field):
    if field[0][0] == field[0][1] == field[0][2] == "x" or field[0][0] == field[0][1] == field[0][
        2] == "0":  # левый столбик
        return True
    elif field[0][1] == field[1][1] == field[2][1] == "x" or field[2][0] == field[2][1] == field[2][
        2] == "0":  # средний столбик
        return True
    elif field[0][2] == field[1][2] == field[2][2] == "x" or field[0][2] == field[1][2] == field[2][
        2] == "0":  # правый столбик
        return True

    elif field[0][0] == field[1][0] == field[2][0] == "x" or field[0][0] == field[1][0] == field[2][
        0] == "0":  # верхняя строчка
        return True
    elif field[2][0] == field[2][1] == field[2][2] == "x" or field[2][0] == field[2][1] == field[2][
        2] == "0":  # нижняя строчка
        return True
    elif field[1][0] == field[1][1] == field[1][2] == "x" or field[1][0] == field[1][1] == field[1][
        2] == "0":  # средняя строчка
        return True

    elif field[0][0] == field[1][1] == field[2][2] == "x" or field[0][0] == field[1][1] == field[2][
        2] == "0":  # основная диагональ
        return True
    elif field[2][0] == field[1][1] == field[0][2] == "x" or field[2][0] == field[1][1] == field[0][
        2] == "0":  # побочная диагональ
        return True


def tie_checker(field_visited):
    summ = 0
    for i in range(3):
        summ += sum(field_visited[i])
    if summ == 9:
        return True
    else:
        return False


def right_print(field):
    for i in range(len(field)):
        print(*field[i])


field = [["." for i in range(3)] for i in range(3)]
field_pos = [[0 for i in range(3)] for i in range(3)]
character = 'x'
move_counter = 0
# field = [[" ", " ", " "], ["x", "x", "x"], [" ", " ", " "]]
for i in range(81):
    if move_counter % 2 == 0:
        character = "x"
    else:
        character = "o"
    print("Ходит", character, "\nВведите координаты (x,y)")
    x, y = map(int, input().split())
    if field_pos[y][x] == 0:
        field[y][x] = character
        field_pos[y][x] = 1
        move_counter += 1
        right_print(field)
        if win_checker(field):
            print("Выиграл", character)
            break
        if tie_checker(field_pos):
            print("Ничья")
    else:
        print("Клетка занята")
