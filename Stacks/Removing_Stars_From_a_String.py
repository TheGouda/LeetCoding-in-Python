class Solution:
    def removeStars(self, string: str) -> str:
        
        stack = []

        for char in string:

            if char == '*' :
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)

object = Solution()
print(object.removeStars("leet**cod*e"))  # Output: "lecoe"