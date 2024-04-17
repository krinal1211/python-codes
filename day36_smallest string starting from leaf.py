class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node, path):
            if not node:
                return
            char = chr(node.val + ord('a'))
            path = char + path
            if not node.left and not node.right:
                self.smallest = min(self.smallest, path)
            dfs(node.left, path)
            dfs(node.right, path)

        self.smallest = '~'  
        dfs(root, '')
        return self.smallest

