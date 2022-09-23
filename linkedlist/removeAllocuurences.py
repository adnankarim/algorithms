# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#time O(2N)
# space O(1)
    
    
    
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        while head!=None and head.val==val:
            head=head.next
        if head==None or head.val==None:
            return head
            
        prev=head
        curr=head.next
       
        while curr!=None:
            if curr.val==val:
                prev.next=curr.next
                curr=curr.next
            else:
                prev=curr
                curr=curr.next
        return head