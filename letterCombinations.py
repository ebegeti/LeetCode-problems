'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''

def letterCombinations( digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    phone = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }

    res = []

    for d in digits:
        new_letters = phone[d]

        cur_len = len(res)

        if not cur_len:
            res.extend(list(new_letters))
        else:
            for i in range(cur_len):
                pre_letters = res.pop(0)
                res.extend([pre_letters + new_letter for new_letter in new_letters])

    print(res)

letterCombinations('23')
