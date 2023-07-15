class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_root_to_leaf_paths(root):
    if root is None:
        return

    stack = [(root, str(root.val))]
    paths = []

    while stack:
        node, path = stack.pop()

        if node.left is None and node.right is None:
            paths.append(path)
        
        if node.right:
            stack.append((node.right, path + "->" + str(node.right.val)))
        
        if node.left:
            stack.append((node.left, path + "->" + str(node.left.val)))

    for path in paths:
        print(path)

# Create the binary tree
root = TreeNode(6)
root.left = TreeNode(3)
root.right = TreeNode(5)
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# Print all root-to-leaf paths
print_root_to_leaf_paths(root)
