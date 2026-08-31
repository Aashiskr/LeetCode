# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        # A list with fewer than 3 nodes cannot have any critical points
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        nxt = curr.next
        
        index = 1
        first_cp = -1
        prev_cp = -1
        min_dist = float('inf')
        
        while nxt:
            # Check if current node is a local maxima or minima
            if (curr.val > prev.val and curr.val > nxt.val) or \
               (curr.val < prev.val and curr.val < nxt.val):
                
                # If this is the first critical point we've found
                if first_cp == -1:
                    first_cp = index
                else:
                    # Update minimum distance using the adjacent critical point
                    min_dist = min(min_dist, index - prev_cp)
                
                # Update the previous critical point to the current index
                prev_cp = index
            
            # Move pointers forward
            prev = curr
            curr = nxt
            nxt = nxt.next
            index += 1
            
        # If min_dist wasn't updated, we found fewer than 2 critical points
        if min_dist == float('inf'):
            return [-1, -1]
            
        # max_dist is the difference between the last and the first critical points
        max_dist = prev_cp - first_cp
        
        return [min_dist, max_dist]