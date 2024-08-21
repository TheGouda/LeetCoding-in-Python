from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if(nums == []):
            return 0
        
        s = set()
        temp = sorted(set(nums))
        n = len(temp)
        lenn = 1

        for i in range(n-1):
            if((temp[i+1]-temp[i]) == 1):
                lenn += 1
            else:
                s.add(lenn)
                lenn = 1
        
        s.add(lenn)
        return max(s)

object = Solution()
print(object.longestConsecutive([100, 4, 200, 1, 3])) #4