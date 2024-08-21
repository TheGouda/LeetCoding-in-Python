from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        for i in nums:
            if(i not in d):
                d[i]=1
            else:
                d[i]+=1
        d = sorted(d, key=d.get, reverse=True)
        l=[]
        for i in range(k):
            l.append(d[i])
        return l

object = Solution()
print(object.topKFrequent([1,1,1,2,2,3], 2))