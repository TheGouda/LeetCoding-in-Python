class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        n = len(s)
        left_ptr, right_ptr = 0, n-1

        while left_ptr < right_ptr :
            if(s[left_ptr] != s[right_ptr]):
                del_left, del_right = s[left_ptr+1:right_ptr+1], s[left_ptr:right_ptr]
                return ((del_left == del_left[::-1]) or (del_right == del_right[::-1]))
            left_ptr, right_ptr = left_ptr + 1, right_ptr - 1
        return True

object = Solution()
print(object.validPalindrome("aba")) # True