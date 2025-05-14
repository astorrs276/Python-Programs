class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    return 0 if root is None else 1 + max(solve(root.left), solve(root.right))