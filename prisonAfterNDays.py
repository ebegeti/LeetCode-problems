'''
There are 8 prison cells in a row and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.

You are given an integer array cells where cells[i] == 1 if the ith cell is occupied and cells[i] == 0 if the ith cell is vacant, and you are given an integer n.

Return the state of the prison after n days (i.e., n such changes described above).
'''

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


prisonAfterNDays([0,1,0,1,1,0,0,1],7)
