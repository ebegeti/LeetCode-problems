'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
'''

def missingNumber( nums):
    """
    :type prices: List[int]
    :rtype: int
    """

    sorted_nums = sorted(nums)
    for i in range(0,len(sorted_nums)):
        if sorted_nums[i] != i:
            return i
    else:
        return len(nums)

print(missingNumber([3,0,1]))
