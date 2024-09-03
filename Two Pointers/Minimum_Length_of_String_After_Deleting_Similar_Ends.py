class Solution:
    def minimumLength(self, s: str) -> int:
        
        n = len(s)
        l_ptr, r_ptr = 0, n-1

        while l_ptr < r_ptr and s[l_ptr] == s[r_ptr]:
            temp = s[l_ptr]
            while l_ptr <= r_ptr and s[l_ptr] == temp:
                l_ptr += 1
            while l_ptr <= r_ptr and s[r_ptr] == temp:
                r_ptr -= 1
        return (r_ptr - l_ptr + 1)

object = Solution()
print(object.minimumLength("aabccabba")) # Output: 3