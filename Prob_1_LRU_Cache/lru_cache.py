import collections

class LRU_Cache(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1


    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if len(self.cache) >= self.cap:
            self.cache.popitem(last=False) # remove oldest
        self.cache[key] = value

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print('get 1', our_cache.get(1), our_cache.cache, our_cache.cap)       # returns 1
print('get 2', our_cache.get(2), our_cache.cache, our_cache.cap)       # returns 2
print('get 9', our_cache.get(9), our_cache.cache, our_cache.cap)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print('get 3', our_cache.get(3), our_cache.cache, our_cache.cap)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

# Test Case 2

# Test Case 3

# Show Me the Data Structures
