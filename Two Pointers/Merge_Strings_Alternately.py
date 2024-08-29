class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0,0
        word1_len = len(word1)
        word2_len = len(word2)
        final = ''

        while i < word1_len and j < word2_len:
            final += word1[i] + word2[j]
            i,j = i+1,j+1
        final+=word1[i:]+word2[j:]
        
        return final

object = Solution()
print(object.mergeAlternately("abc","pqr")) # Output: apbqcr