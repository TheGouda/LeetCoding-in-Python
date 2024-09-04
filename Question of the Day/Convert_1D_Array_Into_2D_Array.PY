from typing import List
import numpy as np # type: ignore

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        arr = np.array(original)
        if(m*n == len(original)):
            res = arr.reshape(m,n)
            return res
        else:
            return []
    
object = Solution()
print(object.construct2DArray([1,2,3,4], 2, 2)) # Output : [[1,2],[3,4]]