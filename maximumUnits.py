'''
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.
'''

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
