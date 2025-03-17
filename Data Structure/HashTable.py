class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def set(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is None:
                continue
            else:
                for j in range(len(self.data_map[i])):
                    keys.append(self.data_map[i][j][0])
        return keys
    
    def print_table(self):
        for i, v in enumerate(self.data_map):
            print(i, ": ", v)

ht = HashTable()
ht.set("bolts", 1400)
ht.set("washers", 50)
ht.set("lumber", 70)

ht.print_table()

print(ht.get("lumber"))
print(ht.get("bolts"))
print(ht.get("bols"))

print(ht.keys())