from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        x, y, direct, res = 0, 0, 0, 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] 
        obstacles = set(map(tuple, obstacles))

        for cmd in commands:
            if cmd == -1:
                direct = (direct + 1) % 4
            elif cmd == -2:
                direct = (direct - 1) % 4
            else:
                dx, dy = directions[direct]
                while cmd:
                    if (x + dx, y + dy) in obstacles:
                        break
                    x, y = x + dx, y + dy
                    cmd -= 1
            res = max(res, x**2 + y**2)

        return res

object = Solution()
print(object.robotSim([4,-1,3], [])) # Output : 25