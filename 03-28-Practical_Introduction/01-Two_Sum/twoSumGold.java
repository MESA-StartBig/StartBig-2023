import java.util.HashMap;
import java.util.Map;
 

// Time Complexity O(N)
// Space Complexity O(N)
//where N = numsSize
class Solution {

    public int[] twoSum(int[] nums, int target) {
        // Create a new hash map that maps numbers to indexes
        Map<Integer, Integer> numToIndex = new HashMap<>();
        
        // For each element in the array we verify if the HashMap already contains the number that
        // "complements" the current i.e. with which the sum between the current number results into the target
        for (int i = 0; i < nums.length; i++) {

            if (numToIndex.containsKey(target - nums[i])) {

                return new int[] {numToIndex.get(target - nums[i]), i};
            }
            // If the number has no complementary in the HasMap, we simply add it to the HashMap
            numToIndex.put(nums[i], i);
        }

        return new int[] {};
    }
}