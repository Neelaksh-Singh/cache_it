import threading
from queue import Queue


class LIFO:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.store = []

    def insert(self, key, value):

        with threading.Lock():

            if key in self.cache:
                self.cache[key] = value

            elif len(self.store) == self.capacity:
                self.remove()
                self.cache[key] = value
                item = (key, value)
                self.store.append(item)

            else:
                self.cache[key] = value
                item = (key, value)
                self.store.append(item)

        # print(self.store)
        # print("================================")
        # print("================================")

    def remove(self):

        key, _ = self.store[-1]
        self.store.pop()
        # print("Key popped : ", key)
        # # print("::::::::::::::::::::::::::::::::::::::::::::")
        # print("::::::::::::::::::::::::::::::::::::::::::::")
        # print(self.store)
        # print("::::::::::::::::::::::::::::::::::::::::::::")
        # print("::::::::::::::::::::::::::::::::::::::::::::")
        self.cache.pop(key)

    def get(self, key):
        with threading.Lock():

            if key in self.cache:

                return self.cache[key]

            else:

                raise KeyError("Not found!")


cc = LIFO(5)
cc.insert(1, 'a')
cc.insert(2, 'b')
cc.insert(3, 'c')
cc.insert(4, 'd')
cc.insert(5, 'e')
cc.get(1)
cc.insert(6, 'f')
