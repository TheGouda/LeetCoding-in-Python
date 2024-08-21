from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        left_sum = 0
        d = {0:1}

        for i in nums:

            left_sum += i
            
            if(left_sum - k in d):
                count += d[left_sum - k]
            
            if(left_sum not in d):
                d[left_sum] = 1
            else:
                d[left_sum] += 1

        return count

object = Solution()
print(object.subarraySum([1,1,1], 2))  # Output:2