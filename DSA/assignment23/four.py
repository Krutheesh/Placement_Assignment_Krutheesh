class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_bottom_view(root):
    if root is None:
        return

    queue = [(root, 0)]
    horizontal_dist_dict = {}

    while queue:
        node, horizontal_dist = queue.pop(0)

        horizontal_dist_dict[horizontal_dist] = node.val

        if node.left:
            queue.append((node.left, horizontal_dist - 1))
        if node.right:
            queue.append((node.right, horizontal_dist + 1))

    bottom_view = [horizontal_dist_dict[dist] for dist in sorted(horizontal_dist_dict.keys())]
    print(' '.join(map(str, bottom_view)))

# Create the binary tree
root = TreeNode(20)
root.left = TreeNode(8)
root.right = TreeNode(22)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(25)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)

# Print the bottom view of the binary tree
print_bottom_view(root)
