import collections

class ListNode:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.left = ListNode()  # Sentinel node at the head
        self.right = ListNode()  # Sentinel node at the tail
        self.left.next = self.right
        self.right.prev = self.left
        self.map = {}  # Key -> node for quick removal
    
    def length(self):
        return len(self.map)

    def pushRight(self, val):
        """Add a node with the given val to the right end."""
        node = ListNode(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev.next = node
        self.right.prev = node

    def popLeft(self):
        """Remove and return the value of the left-most node."""
        if self.left.next == self.right:
            return None  # List is empty
        val = self.left.next.val
        self.pop(val)
        return val

    def pop(self, val):
        """Remove the node with the given val."""
        if val in self.map:
            node = self.map[val]
            prev, next = node.prev, node.next
            prev.next = next
            next.prev = prev
            del self.map[val]

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity  # Capacity of the cache
        self.size = 0  # Current size of the cache
        self.lfuCnt = 0  # Current minimum frequency
        self.valMap = {}  # key -> value
        self.countMap = collections.defaultdict(int)  # key -> frequency count
        self.listMap = collections.defaultdict(LinkedList)  # frequency -> linked list of keys

    def counter(self, key):
        """Update the frequency of the given key."""
        if key not in self.valMap:
            return
        
        # Get the current frequency of the key
        cnt = self.countMap[key]
        
        # Remove the key from its current frequency list
        self.listMap[cnt].pop(key)
        
        # Increment the frequency count for the key
        self.countMap[key] += 1
        newCnt = self.countMap[key]
        
        # Add the key to the new frequency list
        self.listMap[newCnt].pushRight(key)
        
        # If the old frequency list is now empty and was the minimum, update the lfuCnt
        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt += 1

    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        
        # Update the frequency of the key
        self.counter(key)
        
        # Return the value associated with the key
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key in self.valMap:
            # Key is already in the cache, update its value
            self.valMap[key] = value
            # Update its frequency count
            self.counter(key)
        else:
            # Key is not in the cache, need to insert it
            if self.size == self.cap:
                # Cache is full, evict the least frequently used key
                evict_key = self.listMap[self.lfuCnt].popLeft()
                if evict_key is not None:
                    del self.valMap[evict_key]
                    del self.countMap[evict_key]
                    self.size -= 1
            
            # Insert the new key with value and set its frequency to 1
            self.valMap[key] = value
            self.countMap[key] = 1
            self.listMap[1].pushRight(key)
            self.lfuCnt = 1  # Reset the minimum frequency to 1
            self.size += 1
