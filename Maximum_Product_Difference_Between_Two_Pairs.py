from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return abs((nums[0]*nums[1]) - (nums[-1]*nums[-2]))

object = Solution()
print(object.maxProductDifference([5,6,2,7,4]))  # Output:34