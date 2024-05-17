# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def fun(root):
            if not root:
                return 
            if not root.left and not root.right:
                return root.val
            return fun(root.left) and fun(root.right) if root.val==3 else fun(root.left) or fun(root.right)
        return fun(root)
            
                

         
        
        
