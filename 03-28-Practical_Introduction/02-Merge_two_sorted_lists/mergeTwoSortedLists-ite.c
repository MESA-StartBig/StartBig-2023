#include "stdio.h"

/**
 * Definition for singly-linked list.
 * 
 */
struct ListNode {
    int val;
    struct ListNode *next;
};

// Time Complexity O(N+M)
// where N is the length of list1
// and M is the length of list
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    // if list1 happen to be NULL we will simply return list2
    if(list1 == NULL) {
        
        return list2;
    }
	
    // if list2 happen to be NULL we will simply return list1.
    if(list2 == NULL) {
        
        return list1;
    }
    
    // Get the head with the lowest val
    struct ListNode * ptr = list1;
    if(list1 -> val > list2 -> val) {
        
        ptr = list2;
        list2 = list2 -> next;
    
    } else {

        list1 = list1 -> next;
    }
    
    struct ListNode *curr = ptr;
        
	// till one of the list doesn't reaches NULL
    // i.e. iterate until one of the two lists finishes
    while(list1 && list2) {
    
        if(list1 -> val < list2 -> val) {
            
            curr->next = list1;
            list1 = list1 -> next;
        } else {
            
            curr->next = list2;
            list2 = list2 -> next;
        }
        
        curr = curr -> next;            
    }
		
	// adding remaining elements of bigger list
    // iterating until end
    if(!list1) {
        
        curr -> next = list2;
    
    } else {
        
        curr -> next = list1;
    }    
    
    return ptr;   
}