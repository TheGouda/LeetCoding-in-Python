from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

object = Solution()
print(object.majorityElement([3, 2, 3]))  # Output: 3