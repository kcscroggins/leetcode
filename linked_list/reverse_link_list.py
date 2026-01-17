'''
everse Linked List
Easy
Company Tags
Hints
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]

Output: [3,2,1,0]
Example 2:

Input: head = []

Output: []
Constraints:

0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000
'''

# My Solution (Was not correct)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head
        
        if not head.next:
            return head
        
        temp_ptr1 = head.next

        while temp_ptr1:

            if temp_ptr1.next:
                temp_ptr2 = temp_ptr1.next
                temp_ptr1.next = head
                head = temp_ptr1
                temp_ptr1 = temp_ptr2
                temp_ptr2 = temp_ptr2.next
            
            else:
                head = temp_ptr1
                temp_ptr1 = temp_ptr1.next
        
        return head

# Correct Solution:

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head
        
        if not head.next:
            return head
        
        temp_ptr1 = head.next
        head.next = None          # FIX 1: detach old head to avoid cycle

        while temp_ptr1:
            if temp_ptr1.next:
                temp_ptr2 = temp_ptr1.next
                temp_ptr1.next = head
                head = temp_ptr1
                temp_ptr1 = temp_ptr2
            else:
                # FIX 2: still need to reverse the last link
                temp_ptr1.next = head
                head = temp_ptr1
                temp_ptr1 = None  # or temp_ptr1 = temp_ptr1.next
        
        return head

# Neet Code Solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev