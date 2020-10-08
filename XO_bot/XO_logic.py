import variables


def win_checker(field):
    if field[0][0] == field[0][1] == field[0][2] == "x" or field[0][0] == field[0][1] == field[0][
        2] == "o":  # левый столбик
        return True
    elif field[0][1] == field[1][1] == field[2][1] == "x" or field[0][1] == field[1][1] == field[2][
        1] == "o":  # средний столбик
        return True
    elif field[0][2] == field[1][2] == field[2][2] == "x" or field[0][2] == field[1][2] == field[2][
        2] == "o":  # правый столбик
        return True

    elif field[0][0] == field[1][0] == field[2][0] == "x" or field[0][0] == field[1][0] == field[2][
        0] == "o":  # верхняя строчка
        return True
    elif field[2][0] == field[2][1] == field[2][2] == "x" or field[2][0] == field[2][1] == field[2][
        2] == "o":  # нижняя строчка
        return True
    elif field[1][0] == field[1][1] == field[1][2] == "x" or field[1][0] == field[1][1] == field[1][
        2] == "o":  # средняя строчка
        return True

    elif field[0][0] == field[1][1] == field[2][2] == "x" or field[0][0] == field[1][1] == field[2][
        2] == "o":  # основная диагональ
        return True
    elif field[2][0] == field[1][1] == field[0][2] == "x" or field[2][0] == field[1][1] == field[0][
        2] == "o":  # побочная диагональ
        return True


def tie_checker(field_visited):
    summ = 0
    for i in range(3):
        summ += sum(field_visited[i])
    if summ == 9:
        return True
    else:
        return False


def restarting(chat_id):
    variables.filler_symbol.update({chat_id: [" " for i in range(9)]})
    variables.step_counter.update({chat_id: 0})
    variables.field.update({chat_id: [["_" for i in range(3)] for i in range(3)]})
    variables.field_pos.update({chat_id: [[0 for i in range(3)] for i in range(3)]})
