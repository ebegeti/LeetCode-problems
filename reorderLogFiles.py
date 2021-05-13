'''
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.
'''

class Solution(object):
    def reorderLogFiles( logs):
        """
        :type num: int
        :rtype: str
        """

        digit_logs = []
        letter_logs = []
        for log in logs:
            l = log.split(" ")
            identifier, words, wd = l[0], " ".join(l[1:]), "".join(l[1:])
            if wd.isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append([log, words, identifier])

        #it will sort first the letter logs by the words and then by the identifier
        letter_logs.sort(key=lambda t: (t[1], t[2]))
        print([log[0] for log in letter_logs] + digit_logs)
        return ([log[0] for log in letter_logs] + digit_logs)

 
if __name__ == '__main__':
    sol=Solution.reorderLogFiles(logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])
    if sol==["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]:
        print(True)
