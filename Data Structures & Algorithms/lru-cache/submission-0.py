from collections import defaultdict
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.start = None
        self.end = None
        self.cache = defaultdict(int)
        self.nodes = {}
        self.capacity = capacity


    def remove(self, node):
        prev = node.prev
        next = node.next
        if prev:
            prev.next = node.next
        else:
            self.start = next

        if next:
            next.prev = prev
        else:
            self.end = prev            

        node.prev = None
        node.next = None
    
    def append(self, node):
        if self.end:
            self.end.next = node
            node.prev = self.end
            self.end = self.end.next
        else:
            self.end = node
            self.start = node

        if len(self.cache) > self.capacity:
            startNode = self.start
            nextStart = startNode.next
            print(self.start, nextStart)
            if nextStart:
                nextStart.prev = None
            startNode.next = None
            key = startNode.val
            del self.cache[key]
            del self.nodes[key]
            del startNode
            self.start = nextStart            

    
    

    def get(self, key: int) -> int:

        if key in self.cache:
            node = self.nodes[key]
            self.remove(node)
            self.append(node)
            return self.cache[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            self.cache[key] = value
            self.remove(node)
            self.append(node)

        else:
            node = Node(key)
            self.nodes[key] = node
            self.cache[key] = value

            self.append(node)

            




        
                
            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)