class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def has_loop(head):
    slow_ptr = head
    fast_ptr = head

    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        if slow_ptr == fast_ptr:
            return True

    return False

# Example usage
# Create the linked list: 1->2->3->4->5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Create a loop by connecting the tail to the second node (value = 2)
head.next.next.next.next.next = head.next

# Check if the linked list has a loop
has_loop = has_loop(head)

# Print the result
print(has_loop)
