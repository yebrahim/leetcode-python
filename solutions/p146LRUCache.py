class Node:
    def __init__(self, key, val, next, prev):
        self.key, self.val = key, val
        self.next, self.prev = next, prev
        
class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.head, self.tail = Node(-1, -1, None, None), Node(-1, -1, None, -1)
        self.head.next, self.tail.prev = self.tail, self.head
        self.d = {}

    def _movetohead(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = node
        self.head.next = node
        pass

    def get(self, key):
        res = self.d.get(key, -1)
        if res == -1: return res
        self._movetohead(res)
        return res.val

    def set(self, key, value):
        res = self.d.get(key, -1)
        if res != -1:
            res.val = value
            self._movetohead(res)
            return
        if self.capacity == len(self.d):
            lastnode = self.tail.prev
            lastnode.prev.next = lastnode.next
            lastnode.next.prev = lastnode.prev
            del self.d[lastnode.key]
        n = Node(key, value, self.head.next, self.head)
        self.d[key] = n
        self.head.next.prev = n
        self.head.next = n