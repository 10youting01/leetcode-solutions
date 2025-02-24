#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)  # 轉換成 Python list 來顯示

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    ans = sol.reverseList(head)
    print_linked_list(ans)

# @lc code=end

