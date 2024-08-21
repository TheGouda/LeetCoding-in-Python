from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        add_all = sum(nums)
        left = 0
        for i in range(len(nums)):
            right = add_all - left - nums[i]
            if(left == right):
                return i
            else:
                left += nums[i] 
        return -1
    
object = Solution()
print(object.pivotIndex([1,7,3,6,5,6]))