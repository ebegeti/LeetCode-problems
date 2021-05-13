class Solution(object):
    def romanToInt( s):
        """
        :type s: str
        :rtype: int
        """

        dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        exceptions = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        num = 0
        for key in (exceptions):
            if key in s:
                num+=exceptions[key]
                s=s.replace(key,'')
        for char in s:
            num += dictionary[char]
        print(num)

if __name__ == '__main__':
    Solution.romanToInt('IX')