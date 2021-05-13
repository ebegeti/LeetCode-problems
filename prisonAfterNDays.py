def prisonAfterNDays(cells, n):
    """
    :type cells: List[int]
    :type n: int
    :rtype: List[int]
    """
    new_cells = [i for i in cells]
    for i in range(1, n+1):

        print(f"Day {i}:")
        for i in range(1, 6):
            cells[0] = 0
            cells[7] = 0
            if (new_cells[i - 1] == 1 and new_cells[i + 1] == 1) or (new_cells[i - 1] == 0 and new_cells[i + 1] == 0):
                cells[i] = 1
            else:
                cells[i] = 0
        print(cells)
        new_cells = [i for i in cells]

    return cells

    # future_cells = list()
    # if N == 1:
    #     return cells
    #
    # for i in range(len(cells)):
    #     if i == 0 or i == len(cells) - 1:
    #         future_cells.append(0)
    #     else:
    #         if (cells[i - 1] and cells[i + 1]) or (not cells[i - 1] and not cells[i + 1]):
    #             future_cells.append(1)
    #         else:
    #             future_cells.append(0)
    #
    # print(prisonAfterNDays(future_cells, N - 1))

prisonAfterNDays([0,1,0,1,1,0,0,1],7)