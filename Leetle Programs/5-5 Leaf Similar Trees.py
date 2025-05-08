class TreeNode:
        def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

def solve(root):
    def check(node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1
        else:
            return check(node.left) + check(node.right)
    return check(root) == 1 or root is None