from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for i in emails:
            index_1 = i.index('@')
            left, right = i[:index_1], i[index_1:]
            if('+' in left):
                left = left.split('+')[0]
            left = left.replace('.','')
            s.add(left+'@'+right)
        return len(s)

object = Solution()
print(object.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])) #2