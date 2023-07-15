class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_right_view(root):
    if root is None:
        return

    queue = [(root, 0)]
    level_dict = {}

    while queue:
        node, level = queue.pop(0)

        level_dict[level] = node.val

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    right_view = [level_dict[level] for level in sorted(level_dict.keys())]
    print(' '.join(map(str, right_view)))

# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.left.right = TreeNode(8)

# Print the right view of the binary tree
print_right_view(root)
