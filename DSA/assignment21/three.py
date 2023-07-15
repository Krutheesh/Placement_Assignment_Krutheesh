class Node:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None

def convert_to_doubly_linked_list(root):
    global prev
    prev = None
    head = convert_helper(root)
    return head

def convert_helper(node):
    global prev
    if node is None:
        return None

    convert_helper(node.left)

    if prev is None:
        head = node
    else:
        prev.next = node
        node.prev = prev

    prev = node

    convert_helper(node.right)

    return head

# Test the code
# Input binary tree
#         10
#        /   \
#      5      20
#            /  \
#           30   35
root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.right.left = Node(30)
root.right.right = Node(35)

# Convert binary tree to doubly linked list
head = convert_to_doubly_linked_list(root)

# Traverse the doubly linked list
output = ""
current = head
while current is not None:
    output += str(current.val) + " "
    current = current.next

print("Output:")
print(output.strip())
