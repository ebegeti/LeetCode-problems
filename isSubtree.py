'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """
    tree1 = preorder(s)
    tree2 = preorder(t)
    return tree2 in tree1

def preorder(node):
    if node is None:
        return 'null'
    print(' ' + str(node.val) + " " + preorder(node.left) + " " + preorder(node.right))
    return ' ' + str(node.val) + " " + preorder(node.left) + " " + preorder(node.right)

# driver code
#st = "abcd"
#print(isUniqueChars(st))

if __name__ == '__main__':
    a=[3, 4, 5, 1, 2]
    b=[4, 1, 2]
    print(isSubtree(TreeNode(a),TreeNode(b)))
