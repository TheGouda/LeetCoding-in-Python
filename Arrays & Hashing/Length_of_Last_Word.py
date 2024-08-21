class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.split()
        return len(l[-1])

object = Solution()
print(object.lengthOfLastWord("Hello World"))  # Output: 5