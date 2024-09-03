from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        res = score = 0
        n = len(tokens)
        tokens.sort()
        # print(tokens)

        l_ptr, r_ptr = 0, n-1

        while l_ptr <= r_ptr :
            
            if tokens[l_ptr] <= power:
                # print(f"power before - {power}")
                power -= tokens[l_ptr]
                # print(f"power after - {power}")
                score += 1
                # print(f"score - {score}")
                l_ptr += 1
                res = max (res, score)
                # print(f"l - {l_ptr}")
            elif score > 0:
                # print(f"power before - {power}")
                power += tokens[r_ptr]
                # print(f"tokens_r - {tokens[r_ptr]}")
                # print(f"power after - {power}")
                score -= 1
                # print(f"score - {score}")
                r_ptr -= 1        
                # print(f"r - {r_ptr}")
            else:
                # return score
                break        

            # print()

        return res

object = Solution()
print(object.bagOfTokensScore([100, 200, 300, 400], 200)) # Output : 2