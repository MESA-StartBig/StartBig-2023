# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time Complexity: O(N)
# where N is the max(list1 lenght, list2 lenght)
# Space Complexity: O(1)
# 
# Approach: For simplicity, we create a dummy node to which we attach nodes from lists. 
# We iterate over lists using two-pointers approach and build up a resulting list so that values are monotonically increased.
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = dummy = ListNode()
        
        while list1 and list2:               
            
            if list1.val < list2.val:
                
                cur.next = list1
                list1, cur = list1.next, list1
            
            else:
                
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            
            cur.next = list1 if list1 else list2
            
        return dummy.next