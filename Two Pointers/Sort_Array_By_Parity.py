from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        # ptr = 0
        n = len(nums)

        # for num in range(n):
        #     if(nums[num]%2)==0:
        #         nums[ptr] , nums[num] = nums[num] , nums[ptr]
        #         ptr += 1
        
        # return nums

        l_ptr, r_ptr = 0, 0

        for i in range(n):
            if(nums[i] & 0x1 != 0):
                r_ptr += 1
            else:
                nums[l_ptr], nums[i] = nums[i], nums[l_ptr]
                l_ptr, r_ptr = l_ptr+1, r_ptr+1
        
        return nums

object = Solution()
print(object.sortArrayByParity([3,1,2,4]))  # Output - [2,4,3,1]