from collections import defaultdict

class MyHashSet:

    def __init__(self):     
        self.dict_of_nums = defaultdict(int)

    def add(self, key: int) -> None:
        self.dict_of_nums[key] = True

    def remove(self, key: int) -> None:
        self.dict_of_nums[key] = False

    def contains(self, key: int) -> bool:
        return self.dict_of_nums[key]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)