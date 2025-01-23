# Binary Tree Definition
# class TreeNode:
#         def __init__(self, val=0, left=None, right=None):
#                 self.val = val
#                 self.left = left
#                self.right = right

def solve(root):
        def depth(node):
            if node is None:
                return 0
            else:
                return 1 + max(depth(node.left), depth(node.right))
        return depth(root)