'''
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
'''
def findCircleNum(isConnected):
    """
    :type isConnected: List[List[int]]
    :rtype: int
    """
    # cities=len(isConnected)
    # provinces=len(isConnected)
    # for i in range(0,cities):
    #     for j in range(1,cities):
    #         if isConnected[i][i]==isConnected[i][j]:
    #             provinces-=1
    #             isConnected.pop(isConnected[i])
    #             isConnected.pop(isConnected[j])
    # return provinces

    def dfs(start):
        visited.add(start)
        for end in range(len(isConnected)):
            if isConnected[start][end] and end not in visited:
                dfs(end)

    numOfProvinces = 0
    visited = set()  # index of cities
    for start in range(len(isConnected)):
        if start not in visited:
            numOfProvinces += 1
            dfs(start)
    print(numOfProvinces)

findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
