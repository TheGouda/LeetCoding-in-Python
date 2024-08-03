from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sol = []
        temp = nums2
        for i in nums1:
            ind = nums2.index(i)
            if(ind == len(nums2)-1):
                sol.append(-1)
            else:
                temp = nums2[ind+1:]
                c=0
                for j in temp:
                    if(j > i):
                        sol.append(j)
                        break
                    else:
                        c+=1
                if(c==len(temp)):
                    sol.append(-1)
        return sol

object = Solution()
print(object.nextGreaterElement([4,1,2], [1,3,4,2]))