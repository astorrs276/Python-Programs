class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head, n):
    dummy = ListNode(0, head)
    first = second = dummy
    for _ in range(n + 1):
        first = first.next
    while first:
        first, second = first.next, second.next
    second.next = second.next.next
    return dummy.next