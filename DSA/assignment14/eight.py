class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeZeroSumSublists(head):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    cumulative_sum = 0
    cumulative_sums = {}

    while current:
        cumulative_sum += current.val

        if cumulative_sum == 0:
            # Reset the cumulative sum and remove nodes from the linked list
            cumulative_sum = 0
            dummy.next = current.next

        elif cumulative_sum in cumulative_sums:
            # Remove the nodes between the previous occurrence of the same cumulative sum and the current node
            prev = cumulative_sums[cumulative_sum]
            prev.next = current.next

        else:
            cumulative_sums[cumulative_sum] = current

        current = current.next

    return dummy.next


# Create the linked list [1, 2, -3, 3, 1]
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(-3)
node4 = ListNode(3)
node5 = ListNode(1)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Remove consecutive sequences with a sum of zero
result = removeZeroSumSublists(head)

# Print the resulting linked list
current = result
while current:
    print(current.val, end=" ")
    current = current.next

# Output: 3 1
