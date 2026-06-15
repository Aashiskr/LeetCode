# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Edge case: If the list is empty or has only 1 node, returning None deletes it
        if not head or not head.next:
            return None
        
        # Initialize our pointers
        prev = None
        slow = head
        fast = head
        
        # Move fast by 2 and slow by 1
        while fast and fast.next:
            prev = slow             # Keep track of the node before the middle
            slow = slow.next        # Move slow by 1 step
            fast = fast.next.next   # Move fast by 2 steps
            
        # When the loop finishes, 'slow' is pointing to the middle node.
        # We delete it by making 'prev' point to the node AFTER 'slow'.
        prev.next = slow.next
        
        return head