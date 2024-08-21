from typing import List

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = 1
        right = 1

        n = len(nums)
        left_arr = [0]*n
        right_arr = [0]*n

        for i in range(n):
            left_arr[i] = left
            left *= nums[i]

        for j in range(n-1,-1,-1):
            right_arr[j] = right
            right *= nums[j]

        l=[]

        for k in range(n):
            l.append(left_arr[k]*right_arr[k])

        return l

object = Solution()
print(object.productExceptSelf([1,2,3,4]))

