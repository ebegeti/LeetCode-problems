class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = dict()
        pos = 0
        while pos < len(nums):
            if (target - nums[pos]) not in dictionary:
                dictionary[nums[pos]] = pos
                pos += 1
            else:
                return [dictionary[target - nums[pos]], pos]


if __name__ == '__main__':
    print(Solution.twoSum(object,[2,5,3,7,9],9))
