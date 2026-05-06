/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        // Handle edge cases
        if (!head || !head->next || k == 0) {
            return head;
        }
        
        // Step 1: Find the length of the list and the tail node
        ListNode* tail = head;
        int length = 1;
        while (tail->next) {
            tail = tail->next;
            length++;
        }
        
        // Step 2: Form a circular linked list
        tail->next = head;
        
        // Step 3: Find the effective rotations needed
        k = k % length;
        
        // Calculate the position of the new tail
        int stepsToNewTail = length - k;
        
        // Step 4: Traverse to the new tail
        ListNode* newTail = tail; // starting from tail allows us to move exactly stepsToNewTail times
        while (stepsToNewTail--) {
            newTail = newTail->next;
        }
        
        // Step 5: Set the new head and break the circle
        ListNode* newHead = newTail->next;
        newTail->next = nullptr;
        
        return newHead;
    }
};