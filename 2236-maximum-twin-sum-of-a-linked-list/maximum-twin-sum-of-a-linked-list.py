# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the linked list
        # 'slow' is currently pointing to the start of the second half
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # Step 3: Traverse both halves and find the maximum twin sum
        max_twin_sum = 0
        first_half = head
        second_half = prev  # 'prev' is now the head of the reversed second half
        
        while second_half:
            current_sum = first_half.val + second_half.val
            if current_sum > max_twin_sum:
                max_twin_sum = current_sum
                
            # Move both pointers forward
            first_half = first_half.next
            second_half = second_half.next
            
        return max_twin_sum