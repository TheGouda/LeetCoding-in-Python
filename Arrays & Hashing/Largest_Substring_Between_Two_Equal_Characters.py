from collections import defaultdict

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        n = len(s)
        d = defaultdict(list)

        if(len(set(s)) == len(s)):
            return -1
        else:
            for i in range(n):
                d[s[i]].append(i)
            
            maxx = 0
            for key in d:
                diff = abs(d[key][0] - d[key][-1])
                diff = diff - 1
                if(diff > maxx):
                    maxx = diff
            
            # print(d)
            # print(maxx)
            return maxx
        
object = Solution()
print(object.maxLengthBetweenEqualCharacters("aa")) # Output: 0