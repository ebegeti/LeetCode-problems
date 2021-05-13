class Solution(object):
    def maximumUnits( boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        max_units=0
        i=0
        used_size=0
        remained=0
        #sorted(boxTypes, key=itemgetter(1), reverse=True)
        boxTypes.sort(key=lambda x: x[1],reverse=True)
        while used_size<truckSize and i<len(boxTypes):
            if truckSize-used_size<boxTypes[i][0]:
                remained=truckSize-used_size
                break
            max_units += boxTypes[i][0]*boxTypes[i][1]
            used_size+= boxTypes[i][0]
            i+=1
        if remained!=0:
            max_units+=remained*boxTypes[i][1]
        return max_units
if __name__ == '__main__':
    #[[1,3],[2,2],[3,1]]
    #Solution.maximumUnits([[1,3],[2,2],[3,1]],4)
    Solution.maximumUnits([[1, 3], [5, 5], [2, 5], [4, 2], [4, 1], [3, 1], [2, 2], [1, 3], [2, 5], [3, 2]],35)