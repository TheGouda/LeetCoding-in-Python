from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        # print(people);print()
        n = len(people)
        l_ptr, r_ptr = 0, n-1
        count = 0

        while l_ptr <= r_ptr :
            if(people[l_ptr] + people[r_ptr] <= limit):
                # print(f"people[l] - {people[l_ptr]}")
                # print(f"people[r] - {people[r_ptr]}")
                count +=1
                # print(f"count - {count}")
                l_ptr, r_ptr = l_ptr+1, r_ptr-1
            elif(people[l_ptr] + people[r_ptr] > limit):
                # print(f"people[l] - {people[l_ptr]}")
                # print(f"people[r] - {people[r_ptr]}")
                count += 1
                # print(f"count - {count}")
                r_ptr -= 1
            elif l_ptr == r_ptr :
                count += 1
            
            # print()

        return count

object = Solution()
print(object.numRescueBoats([3,2,2,1], 3)) # Output : 3