from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        d = {}

        for i in nums:
            if(i not in d):
                d[i] = 1
            else:
                d[i] += 1

        pairs = 0

        for j in d:
            pairs += int(((d[j])*(d[j]-1))//2)
        
        return pairs

object = Solution()
print(object.numIdenticalPairs([1,2,3,1,1,3])) #4