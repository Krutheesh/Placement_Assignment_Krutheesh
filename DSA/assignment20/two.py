class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def constructBST(arr, index):
    if index >= len(arr) or arr[index] == -1:
        return None

    node = TreeNode(arr[index])
    node.left = constructBST(arr, 2 * index + 1)
    node.right = constructBST(arr, 2 * index + 2)

    return node


def buildBST(arr):
    return constructBST(arr, 0)


def inorderTraversal(root):
    if root is None:
        return []

    result = []
    result.extend(inorderTraversal(root.left))
    result.append(root.val)
    result.extend(inorderTraversal(root.right))

    return result


# Given level order traversal array
arr = [7, 4, 12, 3, 6, 8, 1, 5, 10]

# Build the BST
root = buildBST(arr)

# Perform inorder traversal to verify the BST
inorder = inorderTraversal(root)
print(inorder)  # Output: [1, 3, 4, 5, 6, 7, 8, 10, 12]
