#class Solution(object):
def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    num = ''
    sign = ''
    s = s.strip(' ')
    for char in s:
        if (char == '+' or char == '-') and num == '':
            sign += char
            continue
        if char.isdigit():
            num += char
        elif (char != '+' or char != '-' or char != ' ') and num == '':
            break
        elif (char != '+' or char != '-' or char != ' ') and num != '':
            break
        elif char == ' ' or char == '.' or char == '+' or char == '-':
            break
    if num != '' and (('+-' not in s and '-+' not in s and '++' not in s and '--' not in s) or sign == ''):
        if s.replace('+', '').startswith(num[0]):
            if int(num) < 2 ** 31 - 1:
                return int(num)
            else:
                return (2 ** 31 - 1)
        elif sign[0] == '-' and num in s:
            if (-1) * int(num) > -2 ** (31):
                if int(num) != 0:
                    return ('-' + str(int(num)))
                else:
                    return 0
            else:
                return (-2 ** (31))
    else:
        return (0)

if __name__ == '__main__':
    print(myAtoi("-41a1"))
    print(myAtoi("452 with"))
    print(myAtoi("-42"))
    print(myAtoi("42"))
    print(myAtoi("  -42"))
    print(myAtoi("with vjfh 93"))
    print(myAtoi("-91283472332"))
    print(myAtoi("91283472332"))
    print(myAtoi("3 3"))
    print(myAtoi("3 3.3"))
    print(myAtoi("+--12"))
    print(myAtoi("++++12"))
    print(myAtoi("++ -- 12"))
    print(myAtoi("12"))
    print(myAtoi("+12-12"))
    print(myAtoi("+12 -12"))
    print(myAtoi("00000-42a1234"))
    print(myAtoi("-00545 884"))
    print(myAtoi("  "))
    print(myAtoi("  00000-42a1234"))
    print(myAtoi("-  00 "))
    print(myAtoi("-42a1"))
    print(myAtoi("++42"))
