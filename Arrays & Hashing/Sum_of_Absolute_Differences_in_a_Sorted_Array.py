from itertools import accumulate
from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        n = len(nums)
        # summ = 0
        res = []
        prefix_sum = list(accumulate(nums))

        for i in range(n):
            left_sum = abs(prefix_sum[i] - nums[i])
            right_sum = abs(prefix_sum[-1] - prefix_sum[i])

            left_total = nums[i]*i - left_sum
            right_total = right_sum - nums[i]*(n-i-1)

            res.append(left_total+right_total)

        # for i in range(n):
        #     summ = 0
        #     for j in range(n):
        #         # print(f"i - {i} and j - {j}")
        #         # print(f"ith ele - {nums[i]} and jth ele - {nums[j]}")
        #         summ += abs(nums[i] - nums[j])
        #         # print(summ)
        #         # print()
        #     res.append(summ)
            
        
        return res
    
object = Solution()
print(object.getSumAbsoluteDifferences([2,3,5])) #[4,3,5]