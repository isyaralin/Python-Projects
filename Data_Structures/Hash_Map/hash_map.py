import sys
import re

class Node: 
    def __init__(self, key, value): 
        self.key = key 
        self.value = value 
        self.next = None 
        
        
def my_hash(z): 
    h = 0 
    for c in z: 
        h = (h * 1_000_003 + ord(c)) % (2 ** 32) 
    return h 


class HashMap: 
    def __init__(self): 
        self.bucket_count = 5 
        self.buckets = [None] * self.bucket_count 
        self.size = 0 
        
    def set(self, key, value): 
        if self.size / self.bucket_count > 4: 
            self._resize() 
            
        index = my_hash(key) % self.bucket_count 
        current = self.buckets[index] 
        previous = None 
        
        while current: 
            if current.key == key: 
                current.value = value 
                return 
            previous = current 
            current = current.next 
        node_new = Node(key, value) 
        
        if previous: 
            previous.next = node_new
        else: 
            self.buckets[index] = node_new 
        self.size += 1 
        
    def get(self, key): 
        index = my_hash(key) % self.bucket_count 
        current = self.buckets[index] 
        
        while current:
            if current.key == key: 
                return current.value 
            current = current.next
            
        return None 
    
    def remove(self, key): 
        index = my_hash(key) % self.bucket_count 
        current = self.buckets[index] 
        previous = None 
        while current: 
            if current.key == key: 
                if previous: 
                    previous.next = current.next 
                else: 
                    self.buckets[index] = current.next 
                self.size -= 1 
                return 
            
            previous = current
            current = current.next 
            
    def _resize(self): 
        new_bucket_total = self.bucket_count * 2 
        new_buckets = [None] * new_bucket_total
        
        for i in range(self.bucket_count): 
            current = self.buckets[i] 
            
            while current: 
                new_index = my_hash(current.key) % new_bucket_total 
                node_new = Node(current.key, current.value) 
                node_new.next = new_buckets[new_index] 
                new_buckets[new_index] = node_new 
                current = current.next 
                
        self.bucket_count = new_bucket_total
        self.buckets = new_buckets 
        print(f"resizing to {new_bucket_total} buckets")



word_counts = HashMap()


for line in sys.stdin:
    line = line.strip()
    
    if line == "== END ==":
        break
    
    words = re.findall(r"[A-Za-z]+", line.lower())
    
    for word in words:
        count = word_counts.get(word)
        
        if count is None:
            word_counts.set(word, 1)
        else:
            word_counts.set(word, count + 1)


print(f"unique words = {word_counts.size}")


for line in sys.stdin:
    querya = line.strip()
    if not querya:
        continue
    count = word_counts.get(querya.lower())
    if count is not None:
        print(f"{querya} {count}")
        word_counts.remove(querya.lower()) 
    else:
        print(f"{querya} None")

        
