class Solution:
    def isValid(self, string: str) -> bool:

        stack = []
        bracket_map = { ")":"(", "]":"[", "}":"{" }

        for char in string:
            if char in bracket_map:
                if stack and stack[-1] == bracket_map[char] :
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False
            
object = Solution()
print(object.isValid("()")) # True