class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def postorderTraversal(self,root):
        if not root:
            return([])
        return (self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val])

obj=Solution()
nodes=[1,2,3]
root=TreeNode(nodes)
print(obj.postorderTraversal(root))