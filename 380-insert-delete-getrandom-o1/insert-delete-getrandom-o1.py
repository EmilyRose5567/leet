class RandomizedSet:

    def __init__(self):
        self.array = []
        self.map = {} 
        

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.array) #append to map
        self.array.append(val) #append to array
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.map:
            # Get the index of the element to remove
            idx = self.map[val]
            last_val = self.array[-1]

            # Move the last element into that index
            self.array[idx] = last_val
            self.map[last_val] = idx

            # Remove the last element
            self.array.pop()
            del self.map[val]

            return True
        else: return False
        

    def getRandom(self) -> int:
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()