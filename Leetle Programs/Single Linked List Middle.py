class ListNode:
        def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

def solve(head):
    node = head
    count = 1
    while node.next is not None:
        count += 1
        node = node.next
    node = head
    for i in range(count // 2):
        node = node.next
    return node