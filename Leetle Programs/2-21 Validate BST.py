class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    def test(node):
        listed = [node.val]
        if node.left is not None:
            listed = test(node.left) + listed
        if node.right is not None:
            listed = listed + test(node.right)
        return listed
    if root is None:
        return True
    ordered = test(root)
    return ordered == sorted(ordered) and len(ordered) == len(set(ordered))