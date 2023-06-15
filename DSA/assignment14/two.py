class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseLinkedList(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


def addOne(head):
    # Reverse the linked list
    reversed_head = reverseLinkedList(head)
    current = reversed_head
    carry = 1  # Start with a carry of 1 to add 1 to the number

    while current:
        current.val += carry
        carry = current.val // 10
        current.val %= 10

        if carry == 0:
            break

        current = current.next

    if carry == 1:
        # Insert a new node with value 1 at the end
        current.next = ListNode(1)

    # Reverse the linked list again to get the final result
    result = reverseLinkedList(reversed_head)
    return result


# Create a linked list representing the number 456
head = ListNode(4)
node2 = ListNode(5)
node3 = ListNode(6)

head.next = node2
node2.next = node3

# Add 1 to the linked list number
result = addOne(head)

# Convert the result back to a string representation
number_str = ""
current = result
while current:
    number_str += str(current.val)
    current = current.next

print("Output:", number_str)
