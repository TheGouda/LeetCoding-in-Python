from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        if(bills[0] == 10 or bills[0] == 20):
            return False

        d = {5:0, 10:0, 20:0}

        for i in bills:
            
            if(i == 5):
                d[5] += 1

            
            if(i == 10):
                if(d[5] == 0):
                    # print(False)
                    # break
                    return False
            
                else:
                    d[10] += 1
                    d[5] -= 1
                
            if(i == 20):
                
                if(d[10] == 0 and d[5] >= 3):
                    d[5] -= 3
                    d[20] += 1
                    
                elif(d[10]>=1 and d[5]>=1):
                    d[5] -= 1
                    d[10] -= 1
                    d[20] += 1
                
                else:
                    # print(False)
                    # break
                    return False

        # print(d)
        return True

object = Solution()
print(object.lemonadeChange([5,5,5,10,20])) # False