from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans=[0]*(2*n)
        for i in range(n):
            ans[i]=nums[i]
        for j in range(len(nums)):
            ans[j+n]=ans[j]
        return ans

object = Solution()
print(object.getConcatenation([1,2,1])) 