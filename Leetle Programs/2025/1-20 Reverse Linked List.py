class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head):
    if head is None:
        return None
    value = head.val
    item = head.next
    listed = [value]
    while item is not None:
        value = item.val
        item = item.next
        listed.insert(0, value)
    head = ListNode()
    value = listed.pop(0)
    head.val = value
    current = head
    for item in listed:
        new_node = ListNode()
        current.next = new_node
        current = current.next
        current.val = item
    return head