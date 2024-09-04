from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        l=[]
        for i in arr:
            if(arr.count(i) == 1):
                l.append(i)
        try:
            return l[k-1]
        except :
            return ""        

object = Solution()
print(object.kthDistinct(["d","b","c","b","d","a"], 2))