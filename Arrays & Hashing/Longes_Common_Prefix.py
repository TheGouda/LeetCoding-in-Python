from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs1 = sorted(strs)
        left = strs[0]
        right = strs[-1]
        sol = ''
        for i in range(min(len(left),len(right))):
            if(left[i]!=right[i]):
                return sol
            sol+=left[i]
        return sol

object = Solution()
print(object.longestCommonPrefix(["flower","flow","flight"])) # "fl"