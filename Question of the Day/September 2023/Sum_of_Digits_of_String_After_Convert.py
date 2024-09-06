class Solution:
    def getLucky(self, s: str, k: int) -> int:

        alphabet_dict = {chr(i): (i+1) - 97 for i in range(97, 123)}
        int_str = ''

        for i in s:
            int_str += str(alphabet_dict[i])
        # print(int_str)

        res = 0
        str_man = '+'.join(int_str)

        while k:
            # print(f"str before - {str_man}")
            res = eval(str_man)
            # print(f"res - {res}")
            str_man = '+'.join(str(res))
            # print(f"str after - {str_man}")
            k -= 1
            # print()

        return res

object = Solution()
print(object.getLucky("leetcode", 2))  # Output: 6