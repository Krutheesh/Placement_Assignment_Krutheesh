class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_to_bst(root):
    def inorder_traversal(node):
        if node is None:
            return []
        return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

    def build_bst(values):
        if not values:
            return None
        mid = len(values) // 2
        root = TreeNode(values[mid])
        root.left = build_bst(values[:mid])
        root.right = build_bst(values[mid+1:])
        return root

    sorted_values = inorder_traversal(root)
    sorted_values.sort()
    return build_bst(sorted_values)
# Create the binary tree
root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(8)
root.left.right = TreeNode(4)

# Convert the binary tree to a binary search tree
bst_root = binary_tree_to_bst(root)

# Print the resulting binary search tree
def print_tree(node):
    if node is None:
        return
    print_tree(node.left)
    print(node.val)
    print_tree(node.right)

print_tree(bst_root)
