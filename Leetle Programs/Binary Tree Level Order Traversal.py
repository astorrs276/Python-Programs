# class TreeNode:
#         def __init__(self, val=0, left=None, right=None):
#                 self.val = val
#                 self.left = left
#                 self.right = right

def solve(root):
    if root is None:
        return []
    vals = []
    def check(node, layer):
        if len(vals) == layer:
            vals.append([])
        vals[layer].append(node.val)
        if (node.left is not None):
            check(node.left, layer + 1)
        if (node.right is not None):
            check(node.right, layer + 1)
    check(root, 0)
    return vals