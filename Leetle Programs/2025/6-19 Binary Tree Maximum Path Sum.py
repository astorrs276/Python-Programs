class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    def check(node):
        nonlocal max_sum
        if node is None:
            return 0
        left = max(check(node.left), 0)
        right = max(check(node.right), 0)
        current_sum = node.val + left + right
        max_sum = max(max_sum, current_sum)
        return node.val + max(left, right)

    max_sum = float('-inf')
    check(root)
    return max_sum