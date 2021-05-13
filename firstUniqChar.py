
def firstUniqChar( s):
    """
    :type prices: List[int]
    :rtype: int
    """
    freq = {}
    for char in s:
        if char not in freq.keys():
            freq[char]=1
        else:
            freq[char]+=1
    for letter,frequency in freq.items():
        if frequency==1:
            print('letter %s found 1 time' %letter)
            return s.index(letter)
    return -1


print(firstUniqChar("loveleetcode"))