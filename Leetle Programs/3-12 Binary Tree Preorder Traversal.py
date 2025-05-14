class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    return [] if root is None else [root.val] + solve(root.left) + solve(root.right)