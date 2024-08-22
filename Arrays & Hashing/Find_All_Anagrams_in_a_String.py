from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        n = len(p)
        list_of_indexes = []
        sorted_p = ''.join(sorted(p))

        for i in range(len(s)-n+1):
            small_str = ''.join(sorted(s[i:i+(n)]))
            if(small_str == sorted_p):
                # print(f"mini string - {small_str} and initial index is - {i}")
                # print()
                list_of_indexes.append(i)
            
        return list_of_indexes

object = Solution()
print(object.findAnagrams("abab", "ab")) #[0,1,2]