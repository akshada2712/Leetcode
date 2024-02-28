class MyHashMap:

    def __init__(self):
        self.db = {}
        

    def put(self, key: int, value: int) -> None:
        if key not in self.db: 
            self.db[key] = value 
            
        else:
            self.db[key] = value 

    def get(self, key: int) -> int:
        if key in self.db: 
            return self.db[key] 
        else:
            return -1
        

    def remove(self, key: int) -> None:
        if key in self.db:
            self.db.pop(key)
        
        return self.db

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)