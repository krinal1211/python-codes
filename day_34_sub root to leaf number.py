# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def is_leaf(node):
            return not node.left and not node.right

        def dfs(node, acc_str):
            if not node:
                return 0
            
            acc_str += str(node.val)
            
            if is_leaf(node):
                print(acc_str) 
                return int(acc_str)
            
            return dfs(node.left, acc_str) + dfs(node.right, acc_str)
        
        return dfs(root, "")
