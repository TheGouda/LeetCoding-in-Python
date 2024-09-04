from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        res, mod = 0, (10**9 + 7)
        n = len(nums)

        l_ptr, r_ptr = 0, n-1

        while  l_ptr <= r_ptr:
            if (nums[l_ptr] + nums[r_ptr]) > target:
                r_ptr -= 1
            else:
                res += (2**(r_ptr - l_ptr))
                # res %= mod
                l_ptr += 1
        return res % mod

object = Solution()
print(object.numSubseq([3,5,6,7], 9)) # Output : 9