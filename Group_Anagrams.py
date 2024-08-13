from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if((strs==[""]) or (len(strs)==1)):
            return [strs]
        d={}
        final = []
        for i in strs:
            temp = sorted(i)
            key = ''.join(temp)
            if(key not in d):
                d[key]=[i]
            else:
                d[key].append(i)
        for values in d.values():
            final.append(values)
        return final
    
object = Solution()
print(object.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  # [["bat"],["nat","tan"],["ate","eat","tea"]]