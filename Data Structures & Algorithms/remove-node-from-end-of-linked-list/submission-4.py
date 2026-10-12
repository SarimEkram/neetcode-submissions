# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count = 1
        slow = head
        fast = head
        prev = head

        while fast.next is not None:
            
            if count != n:
                count +=1
                fast = fast.next
            else:
                prev = slow
                fast = fast.next
                slow = slow.next

        if slow is head:
            return head.next
        prev.next = slow.next
        return head
                




        