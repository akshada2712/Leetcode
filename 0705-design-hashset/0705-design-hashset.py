class MyHashSet:

    def __init__(self):
        self.db = set()
        
        

    def add(self, key: int) -> None:
        if key not in self.db:
            self.db.add(key)
        

    def remove(self, key: int) -> None:
        if key in self.db:
            self.db.remove(key)
        return self.db 
        
            
        

    def contains(self, key: int) -> bool:
        if key in self.db:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)