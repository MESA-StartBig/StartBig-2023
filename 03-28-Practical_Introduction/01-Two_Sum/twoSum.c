/**
 * Note: The returned array must be malloced, assume caller calls free().
 * 
 * Time Complexity O(N^2)
 * Space Complexity O(1)
 * where N = numsSize
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    // Allocate the array of two elements, also fixing its size
    int *arr = malloc(2*sizeof(int));
    *returnSize = 2;
    
    // Iterate on each couple of element of the array
    for(int i=0; i < numsSize - 1; ++i) {
        for(int j=i+1; j < numsSize; ++j) {
            // If the target is reached, return the array
            if(nums[i] + nums[j] == target) {
                arr[0] = i; 
                arr[1] = j;
                return arr;
            }
        }
    }
    // Otherwise after all possibilities return an empty array
    return arr;
}

// Another approach is possible (slower than using a HashMap)
// based on ordering the array (Time Complexity O(N log N)) 
// and then using a two pointers approach