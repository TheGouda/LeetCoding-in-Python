from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        set1 = set(nums1)
        set2 = set(nums2)

        # print(set1,set2)

        # first = set1.difference(set2)
        # second = set2.difference(set1)

        return [list(set1-set2),list(set2-set1)]

object = Solution()
print(object.findDifference([1,2,3], [2,4,6])) #[[1,3],[4,6]]