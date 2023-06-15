class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def detectAndRemoveLoop(head):
    if head is None or head.next is None:
        return 0  # No loops removed

    slow = head
    fast = head
    loop_detected = False

    # Move slow and fast pointers until they meet
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            loop_detected = True
            break

    # If loop doesn't exist
    if not loop_detected:
        return 0  # No loops removed

    # Move slow pointer to the head
    slow = head

    # Move both pointers at the same pace until they meet at the loop start node
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    # Unlink the last node to remove the loop
    fast.next = None

    loop_count = 1  # Count the number of loops removed
    loop_node = fast
    while loop_node != fast:
        loop_node = loop_node.next
        loop_count += 1

    return loop_count


# Create a linked list with a loop
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3  # Creating a loop

loops_removed = detectAndRemoveLoop(head)

print("Number of loops removed:", loops_removed)
