# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the half of the linked list by using Floyd cycle detection
        one = head
        two = head
        
        while two and two.next:
            one = one.next
            two = two.next.next

        half = one
        second_half = one.next
        one.next = None

        # reverse the the second half linked list
        pre = None
        cur = second_half

        while cur:
            nex = cur.next
            cur.next = pre

            pre = cur
            cur = nex

        # merge two lined list
        first = head
        second = pre

        while first and second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

        return None

