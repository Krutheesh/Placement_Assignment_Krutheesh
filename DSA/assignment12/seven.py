class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def merge_lists(first, second):
    if first is None:
        return second

    if second is None:
        return first

    current_first = first
    current_second = second

    while current_first is not None and current_second is not None:
        next_first = current_first.next
        next_second = current_second.next

        current_first.next = current_second
        current_second.next = next_first

        current_first = next_first
        current_second = next_second

    second = current_second

    return first

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()

# Example usage
# Create the first linked list: 1 -> 2 -> 3
first = ListNode(1)
first.next = ListNode(2)
first.next.next = ListNode(3)

# Create the second linked list: 4 -> 5 -> 6 -> 7 -> 8
second = ListNode(4)
second.next = ListNode(5)
second.next.next = ListNode(6)
second.next.next.next = ListNode(7)
second.next.next.next.next = ListNode(8)

# Merge the lists
merged = merge_lists(first, second)

# Print the merged list
print_linked_list(merged)

# Print the second list (should be 7 -> 8)
print_linked_list(second)
