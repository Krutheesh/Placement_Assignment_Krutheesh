class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def find_nth_from_end(head, N):
    main_ptr = head
    ref_ptr = head

    # Move ref_ptr N nodes ahead
    for _ in range(N):
        if ref_ptr is None:
            return None
        ref_ptr = ref_ptr.next

    # Move both pointers until ref_ptr reaches the end
    while ref_ptr is not None:
        main_ptr = main_ptr.next
        ref_ptr = ref_ptr.next

    return main_ptr.data

# Example usage
# Create the linked list: 1->2->3->4->5->6->7->8->9
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)

# Find the 2nd node from the end
N = 5
nth_node = find_nth_from_end(head, N)

# Print the result
print(nth_node)
