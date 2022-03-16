
# head의 다음 간선에 연결하여 우선 순위를 높임
# size를 넘어가면 tail에서 가장 가까운 노드를 삭제
class Node:
    def __init__(self,key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
class Cache:
    def __init__(self, max_cache_size:int):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_cache_size = max_cache_size
        self.cache = {}

    def put(self, key, value) -> bool:
        # 초기 세팅
        if self.head is None:
            self.head = Node(None, None)
            self.tail = Node(None, None)
            self.head.next = self.tail
            self.tail.prev = self.head
                
        # 헤드에 연결하여 우선순위를 높일 temp 포인터 선언
        if self.cache.get(key) is None:
            temp = Node(key,value)
            self.cache[key] = temp
            self.size += 1
            
        # 기존 키라면 연결을 끊어줌
        else:
            temp = self.cache[key]
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
        
        # 초기 세팅에서 head와 tail을 연결시켜 줬기 때문에 tail은 계속 뒤로 미뤄짐
        self.head.next.prev = temp
        temp.next = self.head.next
        
        self.head.next = temp
        temp.prev = self.head
        
        # maxsize를 넘어가면 삭제
        if self.size > self.max_cache_size:
            key = self.tail.prev.key
            
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
            del self.cache[key]
            self.size -= 1
              
        return True
    
    def get(self, key):
        if not self.cache.get(key):
            return None
        
        return self.cache.get(key).value
    
    def cache_list(self) -> bool:
        temp = self.head.next
        while temp.next:
            print(temp.key, end=" ")
            temp = temp.next
        return True
    
if __name__ == "__main__":
    cache = Cache(4)
    
    cache.put("foo",["baa"])
    cache.put("foo2",["baa2"])
    cache.put("foo",["baa"])
    cache.put("foo3",["baa3"])
    cache.put("foo4",["baa3"])
    cache.put("foo5",["baa3"])
    cache.put("foo6",["baa3"])
    print(cache.get("foo6"))

    # cache.cache_list()