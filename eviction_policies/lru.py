import threading
import time


class LRU(object):

    def __init__(self, capacity):

        # this variables maps image names to file locations
        self.cache = {}
        self.capacity = capacity

    def insert(self, key, value):
        '''
        Insert a new key,value into our cache. If inserting would exceed our cache size,
        then we shall make room for it by removing the least recently used. 
        '''
        entry_time = time.time()
        with threading.Lock():

            if len(self.cache) == self.capacity:
                self.remove()

            self.cache[key] = [value, entry_time]
        # print(self.cache)
        # print("================================")
        # print("================================")

    def get(self, key):
        '''
        Retrieve an value from our cache, keeping note of the time we last 
        retrieved it. 
        '''
        entry_time = time.time()
        with threading.Lock():

            if key in self.cache:

                self.cache[key][1] = entry_time
                # print(key, self.cache[key])
                # print("##############################")
                # print("##############################")

                return self.cache[key]

            else:

                raise KeyError("Not found!")

    def remove(self, key=None):
        '''
        Will remove the most recently used data.

        Would only be called in a threadsafe context.
        '''
        # scan through and find the least recently used key by finding
        # the lowest timestamp among all the keys.
        with threading.Lock():

            if key:
                self.cache.pop(key, None)
                return
            least_recently_used_key = min(
                self.cache, key=lambda key: self.cache[key][1])

            # now that the least recently used key has been found,
            # remove it from the cache and from our list of request timestamps.
            self.cache.pop(least_recently_used_key)

            # print("::::::::::::::::::::::::::::::::::::::::::::")
            # print("::::::::::::::::::::::::::::::::::::::::::::")
            # print(self.cache)
            # print("::::::::::::::::::::::::::::::::::::::::::::")
            # print("::::::::::::::::::::::::::::::::::::::::::::")

            return


cc = LRU(5)
cc.insert(1, 'a')
cc.insert(2, 'b')
cc.insert(3, 'c')
cc.insert(4, 'd')
cc.insert(5, 'e')
cc.get(1)
cc.insert(6, 'f')
