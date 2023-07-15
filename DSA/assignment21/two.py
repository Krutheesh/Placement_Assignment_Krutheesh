class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def find_distance(root, node1, node2):
    # Find the lowest common ancestor (LCA)
    lca = find_lca(root, node1, node2)

    # Calculate the distances from LCA to node1 and node2
    distance1 = find_distance_to_node(lca, node1, 0)
    distance2 = find_distance_to_node(lca, node2, 0)

    # Return the sum of distances
    return distance1 + distance2

def find_lca(node, node1, node2):
    if node is None:
        return None

    if node.val > node1 and node.val > node2:
        return find_lca(node.left, node1, node2)
    elif node.val < node1 and node.val < node2:
        return find_lca(node.right, node1, node2)
    else:
        return node

def find_distance_to_node(node, target, distance):
    if node is None:
        return -1

    if node.val == target:
        return distance

    if target < node.val:
        return find_distance_to_node(node.left, target, distance + 1)
    else:
        return find_distance_to_node(node.right, target, distance + 1)




root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

# Example 1
node1 = 6
node2 = 14
distance = find_distance(root, node1, node2)
print("The distance between", node1, "and", node2, "=", distance)
# Expected output: The distance between 6 and 14 = 4

# Example 2
node1 = 3
node2 = 4
distance = find_distance(root, node1, node2)
print("The distance between", node1, "and", node2, "=", distance)
# Expected output: The distance between 3 and 4 = 2
