'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''

def wordBreak( s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """

    starts = [0]
    for i in range(len(s)):
        for j in starts:
            if s[j:i + 1] in wordDict:
                starts.append(i + 1)
                break
    print(starts[-1] == len(s))

wordBreak('carsa',['car','sa','sa'])
