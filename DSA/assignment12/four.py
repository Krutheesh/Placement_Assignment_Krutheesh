class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def is_palindrome(head):
    stack = []
    current = head

    # Traverse the linked list and store characters in the stack
    while current is not None:
        stack.append(current.data)
        current = current.next

    # Traverse the linked list again and compare with the top of the stack
    current = head
    while current is not None:
        if current.data != stack.pop():
            return False
        current = current.next

    return True

# Example usage
# Create the linked list: R->A->D->A->R->NULL
head = ListNode('R')
head.next = ListNode('A')
head.next.next = ListNode('D')
head.next.next.next = ListNode('A')
head.next.next.next.next = ListNode('R')

# Check if the linked list is a palindrome
is_palindrome = is_palindrome(head)

# Print the result
if is_palindrome:
    print("Yes")
else:
    print("No")
