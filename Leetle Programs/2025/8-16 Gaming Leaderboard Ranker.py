def solve(board, update):
    def sorter(e):
        return e[1]
    if update[0] in [item[0] for item in board]:
        board = [item for item in board if item[0] != update[0]]
        board.append(update)
        board.sort(reverse=True, key=sorter)
        return board
    else:
        board.append(update)
        board.sort(reverse=True, key=sorter)
        return board