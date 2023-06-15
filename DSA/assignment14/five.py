class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head):
    if head is None or head.next is None:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head

    return head


# Create the linked list [1, 2, 3, 4, 5]
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Group nodes with odd indices together followed by nodes with even indices
reordered = oddEvenList(head)

# Print the reordered list
current = reordered
while current:
    print(current.val, end=" ")
    current = current.next

# Output: 1 3 5 2 4
