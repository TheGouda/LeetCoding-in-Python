class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(s==t):
            return True
        elif((s=="" and t=="") or (s=="" and t!="")):
            return True
        elif(s!="" and t==""):
            return False
        else:
            temp = t
            count = 0
            for i in s:
                if(i not in t):
                    return False
                else:
                    if(i not in temp):
                        return False
                    else:
                        temp_index = temp.index(i)
                        temp = temp[temp_index+1:]
                        count+=1
            if(count==len(s)):
                return True
            else:
                return False

object = Solution()
print(object.isSubsequence("abc", "ahbgdc")) # True