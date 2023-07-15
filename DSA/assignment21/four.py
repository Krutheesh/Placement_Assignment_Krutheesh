class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect_nodes_at_same_level(root):
    if root is None:
        return

    # Queue to perform level order traversal
    queue = [root]

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)

            # Link the node to its right sibling
            if i < level_size - 1:
                node.next = queue[0]

            # Add the left and right children to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return root
# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Connect nodes at the same level
connected_root = connect_nodes_at_same_level(root)

# Print the resulting connections
def print_connections(node):
    if node is None:
        return
    print(node.val, end=' → ')
    if node.next is None:
        print(-1)
    else:
        print(node.next.val)
    print_connections(node.left)
    print_connections(node.right)

print_connections(connected_root)
