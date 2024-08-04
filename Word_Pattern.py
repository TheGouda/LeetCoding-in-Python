class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        p_len = len(p)
        s_trim = s.split()
        s_len = len(s_trim)
        if(p_len!=s_len):
            return False
        elif(len(set(p)) != len(set(s_trim))):
            return False
        else:
            d = {}
            for p_str,s_str in (zip(p,s_trim)):
                if(p_str in d):
                    if(d[p_str]!=s_str):
                        return False
                else:    
                    d[p_str]=s_str
            return True
        
object = Solution()
print(object.wordPattern("abba","dog cat cat dog"))