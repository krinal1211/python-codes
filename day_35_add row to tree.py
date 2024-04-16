# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root       
        queue = [(root, 1)]
        while queue:
            node, node_depth = queue.pop(0)          
            if node_depth == depth - 1:
                left_child = TreeNode(val)
                left_child.left = node.left
                node.left = left_child
                
                right_child = TreeNode(val)
                right_child.right = node.right
                node.right = right_child
                
            elif node_depth < depth - 1:
                if node.left:
                    queue.append((node.left, node_depth + 1))
                if node.right:
                    queue.append((node.right, node_depth + 1))      
        return root
def treeToList(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        current_node = queue.pop(0)
        if current_node:
            result.append(current_node.val)
            queue.append(current_node.left)
            queue.append(current_node.right)
        else:
            result.append(None)
    return result


