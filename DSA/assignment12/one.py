class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def delete_middle_node(head):
    if head is None or head.next is None:
        return None

    slow_ptr = head
    fast_ptr = head
    prev_ptr = None

    while fast_ptr is not None and fast_ptr.next is not None:
        fast_ptr = fast_ptr.next.next
        prev_ptr = slow_ptr
        slow_ptr = slow_ptr.next

    prev_ptr.next = slow_ptr.next

    return head

# Example usage
# Create the linked list: 1->2->3->4->5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Delete the middle node
new_head = delete_middle_node(head)

# Print the modified linked list
current = new_head
while current is not None:
    print(current.data, end=' ')
    current = current.next

