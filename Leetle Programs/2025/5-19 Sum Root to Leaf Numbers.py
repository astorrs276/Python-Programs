class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

sum = 0
def solve(root):
    def check(node, path):
        global sum
        if node is None:
            return
        elif node.left is None and node.right is None:
            sum += int(path + str(node.val))
        else:
            check(node.left, path + str(node.val))
            check(node.right, path + str(node.val))
    check(root, "")
    return sum