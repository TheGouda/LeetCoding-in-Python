from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        l_ptr, time = 0, 0
        n = len(colors)

        for r_ptr in range(1,n) :
            if(colors[l_ptr] == colors[r_ptr]):
                if(neededTime[l_ptr] < neededTime[r_ptr]):
                    time += neededTime[l_ptr]
                    l_ptr = r_ptr
                else:
                    time += neededTime[r_ptr]
            else:
                l_ptr = r_ptr

        return time
                
object = Solution()
print(object.minCost("abaac", [1,2,3,4,5])) # Output : 3