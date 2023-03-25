// Time complexity: O(N)
// where N is the arraySize

// Space complexity: O(1)

// Idea: instead of calculating area by height*width, we can think it in a cumulative way. 
// In other words, sum water amount of each bin(width = 1).
// Search from left to right and maintain a max height of left and right separately, 
// which is like a one-side wall of partial container. Fix the higher one and flow water from the lower part. 
// For example, if current height of left is lower, we fill water in the left bin. 
// Until left meets right, we filled the whole container.
int trap(int* height, int heightSize) {
    
    int left = 0; 
    int right = heightSize - 1;
    int res = 0;
    int maxleft = 0, maxright = 0;
    
    while(left <= right){
        
        if(height[left] <= height[right]) {
            
            if(height[left] >= maxleft) { 
                
                maxleft = height[left];
            
            } else { 
                
                res += maxleft - height[left];
            }
            
            left++;

        } else {
    
            if(height[right] >= maxright) {

                maxright = height[right];

            } else {
                    
                res += maxright - height[right];
            }

            right--;
        }
    }

    return res;
}