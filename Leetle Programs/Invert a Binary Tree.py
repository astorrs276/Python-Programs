# class TreeNode:
#         def __init__(self, val=0, left=None, right=None):
#                 self.val = val
#                 self.left = left
#                 self.right = right

def solve(root):
    def invert(node):
        if node:
            node.left, node.right = invert(node.right), invert(node.left)
        return node
    return invert(root)