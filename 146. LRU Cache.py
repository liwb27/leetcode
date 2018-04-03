# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
import collections

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.data = collections.OrderedDict() #使用有序字典，元素按照添加先后顺序存储

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        value = self.data.pop(key, -1)
        if value != -1: #存在key， 删除再添加，保证在队列开始
            self.data[key] = value
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.data: #检查是否存在元素
            self.data.pop(key)
            self.data[key] = value #删除再添加可以保证新元素在队列开始位置
        else:
            if len(self.data) >= self.capacity: #超出容量，删除最后一个元素
                for k in self.data:
                    del self.data[k]
                    break
            self.data[key] = value 

        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(2,1)
    cache.put(1,1)
    cache.put(2,3)
    cache.get(1)
    cache.put(1,5)
    cache.put(1,2)
    cache.get(1)
    cache.get(2)
