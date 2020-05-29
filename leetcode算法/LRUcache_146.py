from collections import OrderedDict

class LRUcache(OrderedDict):
    def __init__(self,capacity):
        super().__init__()
        self.capacity = capacity
        
    def get(self,key):
        if key not in self:
            return -1
        self.move_to_end(key)#move the "key" element to the last show that it has been used recently 
        return self[key]
    
    def put(self,key,value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)
            #last = True means LIFO(last in first out)后进先出
            #last  = False means FIFO(first in first out)先进先出
            
cache = LRUcache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       # 返回  1
cache.put(3, 3)    # 该操作会使得密钥 2 作废
cache.get(2)       # 返回 -1 (未找到)
cache.put(4, 4)    # 该操作会使得密钥 1 作废
cache.get(1)       # 返回 -1 (未找到)
cache.get(3)       # 返回  3
cache.get(4)       # 返回  4

