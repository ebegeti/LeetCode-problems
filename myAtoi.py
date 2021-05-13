'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
'''

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
