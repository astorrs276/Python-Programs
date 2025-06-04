class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head):
    if not head or not head.next:
        return head
    count = 1
    node = head
    while node:
        count += 1
        node = node.next
    node = head
    for i in range(count // 2 - 1):
        node = node.next
    front = head
    back = node.next
    node.next = None
    nodes = []
    node = back
    while node:
        nodes.insert(0, node)
        node = node.next
    for i in range(len(nodes)):
        nodes[i].next = front.next
        front.next = nodes[i]
        front = front.next.next
    return head