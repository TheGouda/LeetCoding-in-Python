class Solution:
    def isAlnum(self, char):
        if char.isalnum():
            return char
            
    def isPalindrome(self, s: str) -> bool:
        ch = ''
        for i in s:
            if(self.isAlnum(i)):
                ch += i
        stripped = ch.lower()
        
        n = len(stripped)

        left_ptr = 0
        right_ptr = n-1
        
        
        while left_ptr < right_ptr:
            if(stripped[left_ptr] != stripped[right_ptr]):
                print(False)
                break
            
            left_ptr += 1
            right_ptr -= 1
        
        else:
            return True
    
object = Solution()
print(object.isPalindrome("A man, a plan, a canal: Panama"))  # True