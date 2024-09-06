class Solution:
    def findComplement(self, num: int) -> int:
        
        complement = 1
 
        while num*2 > complement:
            num = num ^ complement
            complement = complement << 1
        
        return num

object = Solution()
print(object.findComplement(5))  # Output: 2