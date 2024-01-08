class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
            
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(False)
#         self.key = key
#         self.value = value
#         if key in self.cache:
#             self.cache.update(key, value)
            
#         self.cache[key] = value
#         print(self.cache)
#         if len(self.cache) > self.capacity:
#             self.cache.popitem()
            
        
#         if len(self.cache) < self.capacity:
#             self.cache[key] = value
#         else:
#             print(self.cache)
#             self.cache.popitem()
#             self.cache[key] = value
            
#         return self.cache


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)