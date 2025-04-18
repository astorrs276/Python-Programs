# class TreeNode:
#         def __init__(self, val=0, left=None, right=None):
#                 self.val = val
#                 self.left = left
#                 self.right = right
def solve(root):
    def check(node, left):
        if node is not None and left and node.left is None and node.right is None:
            return node.val
        elif node is not None:
            return check(node.left, True) + check(node.right, False)
        else:
            return 0
    return check(root, False)