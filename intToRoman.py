class Solution(object):
    def intToRoman( num):
        """
        :type num: int
        :rtype: str
        """
        #dictionary = { 'M': 1000,'D': 500,'C': 100,'L': 50, 'X': 10, 'V': 5, 'I': 1, }
        dictionary = {'M': 1000,'CM': 900, 'D': 500,'CD': 400, 'C': 100,'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,'V': 5,'IV': 4, 'I': 1 }
        # list out keys and values separately
        key_list = list(dictionary.keys())
        val_list = list(dictionary.values())
        exceptions = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        s = ''
        for each in val_list:
            if num // each !=0:
                position=val_list.index(each)
                char=key_list[position]
                s=s+char*(num//each)
                num=num-(each)*(num//each)
        print(s)
        return (s)
if __name__ == '__main__':
    Solution.intToRoman(44)