def wordBreak( s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """

    ##it doesnt work for case: cars,[car,ca,rs]
    # for each in wordDict:
    #     if each in s:
    #         s=s.replace(each,'')
    #     if s=='':
    #         return True
    # return False

    starts = [0]
    for i in range(len(s)):
        for j in starts:
            if s[j:i + 1] in wordDict:
                starts.append(i + 1)
                break
    print(starts[-1] == len(s))

wordBreak('carsa',['car','sa','sa'])