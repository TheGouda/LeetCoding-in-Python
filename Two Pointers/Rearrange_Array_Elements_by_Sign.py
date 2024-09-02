from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        pos_list = []
        neg_list = []
        res = []

        for i in nums:
            if(i<0):
                neg_list.append(i)
            else:
                pos_list.append(i)
        
        for pos,neg in zip(pos_list,neg_list):
            res.append(pos)
            res.append(neg)
        
        return res

object = Solution()
print(object.rearrangeArray([3,1,-2,-5,2,-4]))  # Output : [3,-2,1,-5,2,-4]