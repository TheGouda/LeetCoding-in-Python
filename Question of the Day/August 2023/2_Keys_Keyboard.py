import math

class Solution:
    def minSteps(self, n: int) -> int:
        l = []
        
        while n % 2 == 0:
            l.append(2)
            n = n // 2
            
        for i in range(3,int(math.sqrt(n))+1,2):
            
            while n % i== 0:
                l.append(i)
                n = n // i
                 
        if n > 2:
            l.append(n)
    
        # return l
        
        return sum(l)

object = Solution()
print(object.minSteps(14))  # Output: 9