class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def maxSubtreeSum(node):
    global maxSum
    if node is None:
        return 0

    left_sum = maxSubtreeSum(node.left)
    right_sum = maxSubtreeSum(node.right)

    subtree_sum = node.val + left_sum + right_sum

    maxSum = max(maxSum, subtree_sum)

    return subtree_sum


def findMaxSubtreeSum(root):
    global maxSum
    maxSum = float('-inf')

    maxSubtreeSum(root)

    return maxSum


# Constructing the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

result = findMaxSubtreeSum(root)
print(result)  # Output: 28
