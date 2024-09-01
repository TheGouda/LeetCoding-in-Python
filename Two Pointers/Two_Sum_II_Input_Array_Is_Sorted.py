from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)
        l_ptr, r_ptr = 0, n-1
        
        # while r_ptr < n :
        #     if(numbers[l_ptr] + numbers[r_ptr] == target):
        #         return [l_ptr+1,r_ptr+1]
        #     elif(r_ptr == n-1):
        #         l_ptr += 1
        #         r_ptr = l_ptr+1
        #     else:
        #         r_ptr += 1
        
        while l_ptr < r_ptr:
            if(numbers[l_ptr]+numbers[r_ptr] > target):
                r_ptr -= 1
            elif(numbers[l_ptr]+numbers[r_ptr] < target):
                l_ptr +=1
            else:
                return [l_ptr+1, r_ptr+1]

object = Solution()
print(object.twoSum([2,7,11,15],9))  #Output - [1,2]
                