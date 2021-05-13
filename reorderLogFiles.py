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

        # identifiers = []
        # letter_logs = []
        # digit_logs = []
        # for log in logs:
        #     new_list = log.split(' ')
        #     if new_list[1].isdigit():
        #         digit_logs.append(new_list[1:])
        #     else:
        #         letter_logs.append(new_list[1:])
        #     identifiers.append(new_list[0][:-1])
        # letter_logs.sort()
        # digit_logs.sort()
        #
        # print(letter_logs + digit_logs)
if __name__ == '__main__':
    sol=Solution.reorderLogFiles(logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])
    if sol==["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]:
        print(True)