class TreeNode:
        def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

def solve(root):
    def check(node):
        result = []
        if node is None:
            return result
        if node.left is not None:
            result.extend(check(node.left))
        if node.right is not None:
            result.extend(check(node.right))
        result.append(node.val)
        return result
    return check(root)