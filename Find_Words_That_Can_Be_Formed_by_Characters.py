from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        # chars_count = Counter(chars)
        summ = 0

        # for word in words:
        #     word_chars_count = defaultdict(int)
        #     good_string = True
        #     for char in word:
        #         word_chars_count[char] += 1
        #         if((char not in chars_count) or (word_chars_count[char] > chars_count[char])):
        #             good_string = False
        #             break
        #     if(good_string):
        #         summ += len(word)

        for word in words:
            for char in word:
                if(chars.count(char) < word.count(char)):
                    break
            else:
                summ += len(word)

        return summ

object = Solution()
print(object.countCharacters(["hello","world"], "hello world")) # 6