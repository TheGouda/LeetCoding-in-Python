class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        s_sort = sorted(s)
        t_sort = sorted(t)
        if(s_sort == t_sort):
            return True
        return False

object = Solution()
print(object.isAnagram('rat','car'))