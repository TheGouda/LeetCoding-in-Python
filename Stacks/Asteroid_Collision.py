from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for ele in asteroids : 

            while stack and ele < 0 and stack[-1] > 0 :

                diff = ele + stack[-1]

                if diff < 0 :

                    stack.pop()

                elif diff > 0 :

                    ele = 0

                else:

                    ele = 0
                    stack.pop()
            
            if ele : 
                stack.append(ele)

        return stack
                
object = Solution()
print(object.asteroidCollision([5,10,-5]))  # Output: [5,10]