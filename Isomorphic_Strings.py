class Solution:
    def isIsomorphic(self, string1: str, string2: str) -> bool:

        if(len(string1) != len(string2)):
            return False

        dict_string1_to_string2 = {}
        dict_string2_to_string1 = {}

        for char1,char2 in (zip(string1,string2)):
            if(char1 in dict_string1_to_string2):
                if(dict_string1_to_string2[char1] != char2):
                    return False
            else:
                dict_string1_to_string2[char1] = char2

            if(char2 in dict_string2_to_string1):
                if(dict_string2_to_string1[char2] != char1):
                    return False
            else:
                dict_string2_to_string1[char2] = char1

        return True

object = Solution()
print(object.isIsomorphic('egg','add'))