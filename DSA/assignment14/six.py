class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def leftShift(head, k):
    if head is None or head.next is None or k == 0:
        return head

    # Find the k+1th node from the beginning
    count = 1
    kth_node = head
    while count < k and kth_node:
        kth_node = kth_node.next
        count += 1

    if kth_node is None:
        return head  # k is greater than or equal to the length of the linked list

    new_head = kth_node.next
    kth_node.next = None

    # Traverse to the end of the linked list
    current = new_head
    while current.next:
        current = current.next

    # Connect the end of the linked list to the original head
    current.next = head

    return new_head


# Create the linked list [2, 4, 7, 8, 9]
head = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(7)
node4 = ListNode(8)
node5 = ListNode(9)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Left-shift the linked list by 3 nodes
k = 3
shifted = leftShift(head, k)

# Print the shifted list
current = shifted
while current:
    print(current.val, end=" ")
    current = current.next

# Output: 8 9 2 4 7
