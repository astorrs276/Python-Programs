class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    if root is None:
        return True
    def check(a, b):
        if a is None and b is None:
            return True
        elif a is None or b is None or a.val != b.val:
            return False
        elif check(a.left, b.right) and check(b.left, a.right):
            return True
        else:
            return False
    return check(root.left, root.right)