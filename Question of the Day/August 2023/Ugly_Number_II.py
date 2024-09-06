class Solution:

    def genUglyNumbers(self):
        
        set_of_nums = set([1])
        while len(set_of_nums) < 4 * 1690:
            curr_set = set_of_nums.copy()
            for num in set_of_nums:
                curr_set.add(2*num)
                curr_set.add(3*num)
                curr_set.add(5*num)
            set_of_nums = curr_set
        
        ans_list = sorted(list(set_of_nums))
        return ans_list

object = Solution()
print(object.genUglyNumbers(10)) #12 - [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]