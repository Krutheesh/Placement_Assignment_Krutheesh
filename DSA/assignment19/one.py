class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.val <= l2.val:
        merged = l1
        merged.next = mergeTwoLists(l1.next, l2)
    else:
        merged = l2
        merged.next = mergeTwoLists(l1, l2.next)

    return merged

def mergeKLists(lists):
    if not lists:
        return None

    # Merge lists pairwise until only one list remains
    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged = mergeTwoLists(l1, l2)
            merged_lists.append(merged)
        lists = merged_lists

    return lists[0]
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
linkedLists = []

# Convert nested lists to linked lists
for l in lists:
    head = ListNode(l[0])
    current = head
    for i in range(1, len(l)):
        current.next = ListNode(l[i])
        current = current.next
    linkedLists.append(head)

result = mergeKLists(linkedLists)
values = []
while result:
    values.append(result.val)
    result = result.next

print(values)  # Output: [1, 1, 2, 3, 4, 4, 5, 6]
