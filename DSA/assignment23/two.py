class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_left_view(root):
    if root is None:
        return

    queue = [(root, 0)]
    level_dict = {}

    while queue:
        node, level = queue.pop(0)

        if level not in level_dict:
            level_dict[level] = node.val

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    left_view = [level_dict[level] for level in sorted(level_dict.keys())]
    print(' '.join(map(str, left_view)))

# Create the binary tree
root = TreeNode(4)
root.left = TreeNode(5)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(1)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(7)

# Print the left view of the binary tree
print_left_view(root)
