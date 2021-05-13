def exist(board,word):
    result=False
    for r in range(len(board)):
        for c in range(len(board[0])):
            if search(board, r, c, word, 0):
                result=True
                break
    print(result)


def search(board, row, col, word, i):
    if i == len(word):
        return True
    if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
        return False
    if board[row][col] != word[i]:
        return False
    char = board[row][col]
    board[row][col] = " "
    res = search(board, row + 1, col, word, i + 1) \
          or search(board, row, col + 1, word, i + 1) \
          or search(board, row - 1, col, word, i + 1) \
          or search(board, row, col - 1, word, i + 1)
    board[row][col] = char
    return res

exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE")