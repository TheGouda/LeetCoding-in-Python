import random

class RandomizedSet:

    def __init__(self):

        sett = set()
        self.sett = sett
        

    def insert(self, val: int) -> bool:

        if(val not in self.sett):
            self.sett.add(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        
        if(val in self.sett):
            self.sett.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        
        random_index = random.randint(0, len(self.sett) - 1)
        return list(self.sett)[random_index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()