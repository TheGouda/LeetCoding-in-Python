from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l_ptr, r_ptr = 0, 0
        n = len(nums)

        while r_ptr < n :
            count = 1
            while r_ptr+1 < n and nums[r_ptr] == nums[r_ptr+1]:
                r_ptr+=1
                count += 1
            
            minn = min(2, count)
            for _ in range(minn):
                nums[l_ptr] = nums[r_ptr]
                l_ptr += 1
            r_ptr += 1
        
        return l_ptr

object = Solution()
print(object.removeDuplicates([1,1,1,2,2,3,3,3,4,4])) #Output : [1,1,2,2,3,3,4,4]