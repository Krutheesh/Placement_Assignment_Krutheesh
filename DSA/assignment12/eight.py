class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def is_circular(head):
    if head is None:
        return False

    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False

# Example usage
# Create a circular linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 2 (connecting back to node 2)
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next

# Check if the linked list is circular
result = is_circular(head)
if result:
    print("The linked list is circular.")
else:
    print("The linked list is not circular.")
