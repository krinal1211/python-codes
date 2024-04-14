class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def is_leaf(node):
            return node and not node.left and not node.right
        
        def dfs(node, is_left):
            if not node:
                return 0
            if is_leaf(node) and is_left:
                return node.val
            return dfs(node.left, True) + dfs(node.right, False)
        
        return dfs(root, False)
