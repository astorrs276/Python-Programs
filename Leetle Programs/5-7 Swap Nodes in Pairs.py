class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head):
    if head is None:
        return head
    node = head
    start = ListNode(0, head)
    current = start
    while node is not None:
        a = node.val
        node = node.next
        if node is None:
            current.next = ListNode(a)
            break
        b = node.val
        node = node.next
        current.next = ListNode(b, ListNode(a))
        current = current.next.next
    return start.next