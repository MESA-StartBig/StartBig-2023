#include "stdio.h"

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    struct ListNode *next;
};

// Time Complexity O(N+M)
// where N is the length of list1
// and M is the length of list
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    // if list1 happen to be NULL we will simply return list2
	if(list1 == NULL) {
		
		return list2;
	}
		
	// if list2 happen to be NULL we will simply return list1
	if(list2 == NULL) {
		
		return list1;
	} 
		
	// if value pointed by list1 pointer is less than or equal to value pointed by list2 pointer
	// we will call recursively list1 -> next and whole list2 list
	if(list1 -> val <= list2 -> val) {
		
		list1 -> next = mergeTwoLists(list1 -> next, list2); // update next element of l1
		return list1; // return pointer to current element
	
	} else {
		
		list2 -> next = mergeTwoLists(list1, list2 -> next);
		return list2;            
	}
}