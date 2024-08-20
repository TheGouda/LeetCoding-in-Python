class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

object = Solution()
print(object.strStr("hello", "ll"))  # Output: 2