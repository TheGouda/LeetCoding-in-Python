from typing import Counter, List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = len(nums)
        count_of_nums = Counter(nums)
        # return count_of_nums
        
        check = n//3
        res = []
        
        for i in count_of_nums:
            if(count_of_nums[i] > check):
                res.append(i)
        
        return res

object = Solution()
print(object.majorityElement([3,2,3]))  # [3]