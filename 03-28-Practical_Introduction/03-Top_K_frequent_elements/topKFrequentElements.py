# Time complexity: O(N log K)
# where N is the number of elements in nums and 
# k is the number of unique elements in the array
# 
# Space Complexity: O(N)
# where N is the number of elements in nums
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element using a hash map
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Step 2: Use a min-heap to store the top k frequent elements
        heap = []
        for num, count in freq.items():
            
            if len(heap) < k:
                
                heapq.heappush(heap, (count, num))
            
            elif count > heap[0][0]:
                
                heapq.heappushpop(heap, (count, num))
                
                # Alternatively (a little slower)
                # heapq.heappop(heap)
                # heapq.heappush(heap, (count, num))
        
        # Step 3: Return the elements in the heap
        return [num for count, num in heap]
    
# link to a solution with lower Time Complexity: https://leetcode.com/problems/top-k-frequent-elements/solutions/1927648/one-of-the-best-explanation/