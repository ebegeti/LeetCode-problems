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