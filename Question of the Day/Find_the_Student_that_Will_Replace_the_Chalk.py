from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:

        chalk_sum = sum(chalk)

        k = k % chalk_sum

        for i in range(len(chalk)):
            if(k < chalk[i]):
                return i
            k -= chalk[i]

object = Solution()
print(object.chalkReplacer([3,4,1,2], 25)) # Output : 1