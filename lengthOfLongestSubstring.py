'''
Given a string s, find the length of the longest substring without repeating characters.
'''
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    substrings = []
    max_length = 0
    for each in s:
        if each in substrings:
            substrings = substrings[substrings.index(each) + 1:]

        substrings.append(each)
        max_length = max(max_length, len(substrings))
    print(max_length)
    return max_length

lengthOfLongestSubstring('bcabcacab')
