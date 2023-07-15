class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DoublyLinkedListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

def binary_tree_to_dll(root):
    def convert_to_dll(node):
        nonlocal prev, head

        if node is None:
            return

        # Recursively convert left subtree
        convert_to_dll(node.left)

        # Process current node
        if prev is None:
            head = DoublyLinkedListNode(node.val)
            prev = head
        else:
            new_node = DoublyLinkedListNode(node.val)
            prev.next = new_node
            new_node.prev = prev
            prev = new_node

        # Recursively convert right subtree
        convert_to_dll(node.right)

    if root is None:
        return None

    head = None
    prev = None
    convert_to_dll(root)

    return head
# Create the binary tree
root = TreeNode(10)
root.left = TreeNode(12)
root.right = TreeNode(15)
root.left.left = TreeNode(25)
root.left.right = TreeNode(30)
root.right.left = TreeNode(36)

# Convert the binary tree to a doubly linked list
dll_head = binary_tree_to_dll(root)

# Traverse the resulting doubly linked list forwards
def traverse_dll_forward(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()

# Traverse the resulting doubly linked list backwards
def traverse_dll_backward(head):
    while head and head.next:
        head = head.next
    while head:
        print(head.val, end=' ')
        head = head.prev
    print()

# Print the resulting doubly linked list forwards and backwards
traverse_dll_forward(dll_head)
traverse_dll_backward(dll_head)
