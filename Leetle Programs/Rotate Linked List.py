class ListNode:
        def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

def solve(head, k):
    if (head is None):
        return head
    elif (head.next is None):
        return head
    for i in range(k):
        last = None
        node = head
        while(node.next != None):
            last = node
            node = node.next
        new_node = ListNode(node.val, head)
        last.next = None
        head = new_node
    return head