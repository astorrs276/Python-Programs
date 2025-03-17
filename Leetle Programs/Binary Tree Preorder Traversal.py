# class TreeNode:
#         def __init__(self, val=0, left=None, right=None):
#                 self.val = val
#                 self.left = left
#                 self.right = right

def solve(root):
    vals = []
    if root is not None:
        vals.append(root.val)
        vals.extend(solve(root.left))
        vals.extend(solve(root.right))
        return vals
    else:
        return []