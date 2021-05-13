'''
A newly designed keypad was tested, where a tester pressed a sequence of n keys, one at a time.

You are given a string keysPressed of length n, where keysPressed[i] was the ith key pressed in the testing sequence, and a sorted list releaseTimes, where releaseTimes[i] was the time the ith key was released. Both arrays are 0-indexed. The 0th key was pressed at the time 0, and every subsequent key was pressed at the exact time the previous key was released.

The tester wants to know the key of the keypress that had the longest duration. The ith keypress had a duration of releaseTimes[i] - releaseTimes[i - 1], and the 0th keypress had a duration of releaseTimes[0].

Note that the same key could have been pressed multiple times during the test, and these multiple presses of the same key may not have had the same duration.

Return the key of the keypress that had the longest duration. If there are multiple such keypresses, return the lexicographically largest key of the keypresses.
'''

class Solution(object):
    def slowestKey( releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """

        #using collection bcs dict has unique values and we dont want that
        i = 1
        from collections import defaultdict

        duration = defaultdict(list)
        duration[keysPressed[0]]=releaseTimes[0]
        maxi=releaseTimes[0]
        char_maxi=keysPressed[0]
        while i < len(releaseTimes):
            duration[keysPressed[i]]=releaseTimes[i]-releaseTimes[i-1]
            #duration.append(releaseTimes[i]-releaseTimes[i-1])
            if duration[keysPressed[i]]>maxi:
                maxi=duration[keysPressed[i]]
                char_maxi=keysPressed[i]
            elif duration[keysPressed[i]]==maxi:
                #means keypressed is larger
                if sorted(keysPressed[i]+char_maxi)==[char_maxi,keysPressed[i]]:
                    char_maxi = keysPressed[i]
            i+=1
        return char_maxi


if __name__ == '__main__':
    # [9, 29, 49, 50]
    # "cbcd"
    # [12, 23, 36, 46, 62]
    # "spuda"
    # [23, 34, 43, 59, 62, 80, 83, 92, 97]
    # "qgkzzihfc"
    # [19, 22, 28, 29, 66, 81, 93, 97]
    # "fnfaaxha"
    releaseTimes =  [23, 34, 43, 59, 62, 80, 83, 92, 97]
    keysPressed =  "qgkzzihfc"
    print(Solution.slowestKey(releaseTimes,keysPressed))
