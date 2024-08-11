from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = nums.count(val)
        for i in range(c):
            nums.remove(val)
        return len(nums)

object = Solution()
print(object.removeElement([3,2,2,3],3)) #2