class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {}
        for i in text:
            if(i=='b' or i=='a' or i=='l' or i=='o' or i=='n'):
                if(i in d):
                    d[i]+=1
                else:
                    d[i]=1
        if(('b' in d) and ('a' in d) and ('l' in d) and ('o' in d) and ('n' in d)):
            l = [d['b'],d['a'],d['l']//2,d['o']//2,d['n']]
            return min(l)
        else:
            return 0
        
object = Solution()
print(object.maxNumberOfBalloons("nlaebolko"))  # Output: 1


            
            