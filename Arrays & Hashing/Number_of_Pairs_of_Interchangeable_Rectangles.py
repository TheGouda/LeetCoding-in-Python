from typing import List

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:

        n = len(rectangles)
        
        # count = 0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if(rectangles[i][0]/rectangles[i][1] == rectangles[j][0]/rectangles[j][1]):
        #             count += 1
        # return count

        dict_of_ratios = {}
        total_pairs = 0

        for i in range(n):
            ratio = rectangles[i][0]/rectangles[i][1]
            if(ratio not in dict_of_ratios):
                dict_of_ratios[ratio] = 1
            else:
                dict_of_ratios[ratio] += 1

        for j in dict_of_ratios:
            
            combination = int((dict_of_ratios[j])*(dict_of_ratios[j] - 1)/2)
            total_pairs += combination

        return total_pairs
    
object = Solution()
print(object.interchangeableRectangles([[4,8],[3,6],[10,20],[15,30]])) #6