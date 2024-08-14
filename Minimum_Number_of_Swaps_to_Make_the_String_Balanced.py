class Solution:
    def minSwaps(self, s: str) -> int:

        extra_close, max_count_close = 0 , 0

        for i in s:
            if(i == '['):
                extra_close -= 1 
            else:
                extra_close += 1

            max_count_close = max(extra_close,max_count_close)
        
        return (max_count_close + 1)//2

object = Solution()
print(object.minSwaps("]]]]]")) # 3