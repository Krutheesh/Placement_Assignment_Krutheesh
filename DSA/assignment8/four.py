class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(s):
    if not s:
        return None

    stack = []
    root = None
    i = 0

    while i < len(s):
        if s[i] == '(':
            stack.append(root)
            i += 1
        elif s[i] == ')':
            root = stack.pop()
            i += 1
        else:
            j = i
            while j < len(s) and s[j] != '(' and s[j] != ')':
                j += 1
            node = TreeNode(int(s[i:j]))

            if not root:
                root = node
            else:
                if not root.left:
                    root.left = node
                else:
                    root.right = node

            root = node
            i = j

    return root

# Example usage:
s = "4(2(3)(1))(6(5))"
root = buildTree(s)

def preorderTraversal(root):
    if not root:
        return []

    result = []

    def preorder(node):
        if node:
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)

    preorder(root)
    return result

preorder = preorderTraversal(root)
print(preorder)  # Output: [4, 2, 3, 1, 6, 5]
