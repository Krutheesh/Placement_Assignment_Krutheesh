class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def traverse_and_delete(head, M, N):
    current = head
    while current is not None:
        # Traverse M nodes
        for _ in range(M - 1):
            if current is None:
                return
            current = current.next
        
        if current is None:
            return
        
        # Delete N nodes
        temp = current
        for _ in range(N):
            if temp.next is None:
                break
            temp = temp.next
        current.next = temp.next
        current = current.next

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()

# Example usage
# Create the linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)

# Traverse the linked list and delete nodes
M = 3
N = 2
traverse_and_delete(head, M, N)

# Print the modified linked list
print_linked_list(head)
