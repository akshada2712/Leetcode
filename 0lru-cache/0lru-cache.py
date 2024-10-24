class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None 
    
    
class LRUCache:
    
    
    # WE will use DLL 
    
    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {}   # dictionary to store node pointers 
        
        self.left, self.right = Node(0, 0), Node(0,0)   #initialize left and right pointers for insertion
        self.left.next, self.right.prev = self.right, self.left # connecting left and right l -> <- r
        
    def remove(self, node):
        prev, nxt = node.prev, node.next 
        prev.next, nxt.prev = nxt, prev 
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right 
        prev.next = nxt.prev = node 
        node.next, node.prev = nxt, prev 
    
    def get(self, key: int) -> int: 
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val 
        
        return -1 
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.left.next 
            self.remove(lru)   # removing first node
            del self.cache[lru.key]
        
    
    
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.dic = collections.OrderedDict()
        

#     def get(self, key: int) -> int:
#         if key not in self.dic:
#             return -1
        
#         self.dic.move_to_end(key)
#         return self.dic[key]
        

#     def put(self, key: int, value: int) -> None:
        
#         if key in self.dic:
#             self.dic.move_to_end(key)
#         self.dic[key] = value
#         if len(self.dic) > self.capacity:
#             self.dic.popitem(False)
            
        
            
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)