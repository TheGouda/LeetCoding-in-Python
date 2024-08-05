from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)): 
            temp = target - nums[i]
            if(temp not in d):
                d[nums[i]] = i
            else:
                return [d[temp],i]

object = Solution()
print(object.twoSum([2, 7, 11, 15], 9))