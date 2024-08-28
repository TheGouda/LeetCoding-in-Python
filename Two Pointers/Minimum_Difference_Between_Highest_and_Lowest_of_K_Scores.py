from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        n = len(nums)
        nums.sort()

        left_ptr , right_ptr = 0 , k - 1
        ans = float('inf')

        while right_ptr < n:
            ans = min(ans, nums[right_ptr] - nums[left_ptr])
            left_ptr , right_ptr = left_ptr + 1 , right_ptr + 1
        
        return ans

object = Solution()
print(object.minimumDifference([1, 2, 3], 2))  # Output: 1