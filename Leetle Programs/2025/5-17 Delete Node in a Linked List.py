class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head, n):
    start = ListNode(0, head)
    last = start
    node = head
    while node.val != n:
        last = node
        node = node.next
    last.next = node.next
    return start.next