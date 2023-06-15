class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def nextLargerNodes(head):
    # Convert the linked list into an array
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next

    stack = []
    result = [0] * len(arr)

    # Traverse the array in reverse order
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]

        while stack and stack[-1] <= num:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(num)

    return result


# Create the linked list [2, 1, 5]
head = ListNode(2)
node2 = ListNode(1)
node3 = ListNode(5)

head.next = node2
node2.next = node3

# Find the next greater node for each node
result = nextLargerNodes(head)

print(result)  # Output: [5, 5, 0]
