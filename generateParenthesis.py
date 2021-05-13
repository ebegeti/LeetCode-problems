'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''
def generateParenthesis( n):
    results = []

    def helper(sofar, results, left, right):
        if left == 0 and right == 0:
            results.append(sofar)
        if left > 0:
            helper(sofar + "(", results, left - 1, right)
        if right > left:
            helper(sofar + ")", results, left, right - 1)

    helper('', results, n, n)
    print(results)

generateParenthesis(3)
