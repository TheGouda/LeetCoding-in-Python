from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i in d:
                return True
            d[i]=1
        
        return False

object = Solution()
print(object.nextGreaterElement([1,2,3,1]))