# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            one = head
            two = head
        else:
            return False

        while two and two.next:
            one = one.next
            two = two.next.next
            if one == two:
                return True

        return False