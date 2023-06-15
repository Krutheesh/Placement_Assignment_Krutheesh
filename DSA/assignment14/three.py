class ListNode:
    def __init__(self, val=0, next=None, bottom=None):
        self.val = val
        self.next = next
        self.bottom = bottom


def mergeTwoLists(list1, list2):
    # Base cases
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    # Create a dummy node to hold the merged list
    dummy = ListNode()
    current = dummy

    # Merge the lists while maintaining the sorted order
    while list1 and list2:
        if list1.val <= list2.val:
            current.bottom = list1
            list1 = list1.bottom
        else:
            current.bottom = list2
            list2 = list2.bottom
        current = current.bottom

    # Append any remaining nodes
    if list1:
        current.bottom = list1
    elif list2:
        current.bottom = list2

    return dummy.bottom


def flattenLinkedList(head):
    # Base case: empty list or only one node
    if head is None or head.next is None:
        return head

    # Recursively flatten the remaining list
    head.next = flattenLinkedList(head.next)

    # Merge the current list with the flattened list of the next node
    head = mergeTwoLists(head, head.next)

    return head


# Create the linked list with sub-linked lists
head = ListNode(5)
node2 = ListNode(10)
node3 = ListNode(19)
node4 = ListNode(28)

head.next = node2
node2.next = node3
node3.next = node4

head.bottom = ListNode(7)
head.bottom.bottom = ListNode(8)
head.bottom.bottom.bottom = ListNode(30)

node2.bottom = ListNode(20)

node3.bottom = ListNode(22)
node3.bottom.bottom = ListNode(50)

node4.bottom = ListNode(35)
node4.bottom.bottom = ListNode(40)
node4.bottom.bottom.bottom = ListNode(45)

# Flatten the linked list
flattened = flattenLinkedList(head)

# Print the flattened list using the bottom pointer
current = flattened
while current:
    print(current.val, end="-> ")
    current = current.bottom

# Output: 5-> 7-> 8-> 10-> 19-> 20-> 22-> 28-> 30-> 35-> 40-> 45-> 50->
