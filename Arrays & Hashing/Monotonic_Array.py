from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if((sorted(nums) == nums) or (list(reversed(sorted(nums))) == nums)):
            return True
        else:
            return False
    
object = Solution()
print(object.isMonotonic([1, 2, 2, 3])) # True