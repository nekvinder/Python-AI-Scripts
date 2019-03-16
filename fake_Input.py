input_board = """
1
4
5
""".split("\n")
i = 0


def input():
    global i, input_board
    i = i + 1
    return input_board[i]
