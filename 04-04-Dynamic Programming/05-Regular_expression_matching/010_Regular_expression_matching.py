# To solve this problem, we have to go through all possible states.
# A state is defined by s_index and p_index, where they define current char from s and p strings.

# We return True if both s_index and p_index are out of bounds (it means that we were able to construct s string from p pattern and there are no chars left in p).
# If s_index is out of bounds, but p_index is not, it means that we were able to construct s string from p, but there are some chars left in p.
# We can delete them only if there are only letter + star pairs left.
# If there is at least one letter (or dot) without star after it, then we have to return False.

# For example if we have s = abc and p = abcz*b*, then we are able to remove z and b occurencies, because there is star after z and after b, so we return True.

# If p_index is out of bounds while s_index is still not out of bounds, it means that we are not able to construct s from p, because there are no letters left, so we return False.

# Then there are 4 options:
# 1. If next char in p is a star and char in s match char in p (if char in p is dot, then we assume that we change dot to the char that is in s) then we have two options: we can use current char in p to match char in s or go to next char in p (because next char is a star, so we can use previous char 0 or more times).
# 2. If next char in p is a star and char in s DOES NOT match char in p, then we can only explore going to the next char in p option (so we increase p_index by 2, because we have to skip the star).
# 3. If next char in p IS NOT a star and char in s match char in p, then we can only explore current char option to match char in s (so we increase both p_index and s_index by 1)
# 4. If next char in p IS NOT a star and char in s DOES NOT match char in p, then there is no option left, so we have to return False.

# We will use memory to store previous state and at the start of the function we check if current state was already explored.
# If yes then we just return value stored in memory.



class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memory = {}
        
        def explore_state(s_index, p_index):
            if (s_index, p_index) in memory:
                return memory[(s_index, p_index)]
            
            s_index_out_of_border = s_index >= len(s)
            p_index_out_of_border = p_index >= len(p)
            next_char_is_a_star = p_index+1 < len(p) and p[p_index+1] == "*"
            
            if s_index_out_of_border is True:
                if p_index_out_of_border is True:
                    return True
                elif next_char_is_a_star is True:
                    memory[(s_index, p_index)] = explore_state(s_index, p_index+2)
                    return memory[(s_index, p_index)]
                else:
                    memory[(s_index, p_index)] = False
                    return memory[(s_index, p_index)]
                
            if p_index_out_of_border:
                return False
            
            match = s[s_index] == p[p_index] or p[p_index] == "."
            
            if next_char_is_a_star is True and match is True:
                memory[(s_index, p_index)] = explore_state(s_index, p_index+2) or explore_state(s_index+1, p_index)
            elif next_char_is_a_star is True and match is False:
                memory[(s_index, p_index)] = explore_state(s_index, p_index+2)
            elif next_char_is_a_star is False and match is True:
                memory[(s_index, p_index)] = explore_state(s_index+1, p_index+1)
            elif next_char_is_a_star is False and match is False:
                memory[(s_index, p_index)] = False
				
            return memory[(s_index, p_index)]
        
        return explore_state(0, 0)