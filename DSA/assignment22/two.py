class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flip_binary_tree(root):
    if root is None or (root.left is None and root.right is None):
        return root

    flipped_left = flip_binary_tree(root.left)
    flipped_right = flip_binary_tree(root.right)

    root.left = flipped_right
    root.right = flipped_left

    return root
# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Flip the binary tree
flipped_root = flip_binary_tree(root)

# Print the flipped binary tree
def print_tree(node):
    if node is None:
        return
    print(node.val)
    print_tree(node.left)
    print_tree(node.right)

print_tree(flipped_root)
