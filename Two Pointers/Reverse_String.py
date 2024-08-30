from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        n = len(s)
        left_ptr, right_ptr = 0, n-1

        while left_ptr < right_ptr:
            s[left_ptr] , s[right_ptr] = s[right_ptr], s[left_ptr]
            left_ptr, right_ptr = left_ptr + 1, right_ptr - 1
        
        return s

object = Solution()
print(object.reverseString(["h","e","l","l","o"]))  # Output: ["o","l","l","e","h"]