# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        def funn(node):
            if not node:
                return None
          
            node.left = funn(node.left)
            node.right = funn(node.right)

            if not node.left and not node.right and node.val == target:
                return None
            return node
        

        return funn(root)
