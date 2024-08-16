class Solution:
    def largestGoodInteger(self, num: str) -> str:

        strr = ''

        flag = False
        s = set()

        for digit in range(len(num)-2):
            if((num[digit] == num[digit+1]) and (num[digit+1] == num[digit+2])):
                strr += num[digit]+num[digit+1]+num[digit+2]
                flag = True
                s.add(strr)
                strr = ''

        if(flag):
            return max(s)
        else:
            return ''
                        
object = Solution()
print(object.largestGoodInteger("6777133339"))  # Output: "777"