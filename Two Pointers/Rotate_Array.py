from typing import List

class Solution:

    def reverse(self,nums,l,r):

        while l < r :
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        
        # return nums


    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        l_ptr, r_ptr = 0, n-1

        self.reverse(nums,l_ptr,r_ptr)

        l_ptr, r_ptr = 0, k-1

        self.reverse(nums,l_ptr,r_ptr)

        l_ptr, r_ptr = k, n-1

        self.reverse(nums,l_ptr,r_ptr)

        # while k :
        #     ele = nums.pop()
        #     nums.insert(0,ele)
        #     k-=1
        

object = Solution()
print(object.rotate([1,2,3,4,5,6,7],3)) # Output : [5,6,7,1,2,3,4]