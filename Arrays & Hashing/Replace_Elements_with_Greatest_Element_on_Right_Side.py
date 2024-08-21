from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if(n==1):
            return [-1]
        elif(n==2 and (arr[-1])==-1):
            return arr
        else:
            maxi = -1
            for i in range(n-1,-1,-1):
                replace = maxi
                if(arr[i]>maxi):
                    maxi = arr[i]
                arr[i] = replace
        return arr

object = Solution()
print(object.replaceElements([17,18,5,4,6,1])) 