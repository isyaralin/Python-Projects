class CircularQueue:
    def __init__(self, size):
        # Create an empty array to add 
        self.size = size
        self.queue = [None] * size
        self.head = 0
        self.end = 0
        self.count_elements = 0  
        self.tot = 0  

    def new_siz(self):
        # If you double it you can resize it 
        new_size = self.size * 2
        updated_queue = [None] * new_size

        
        for i in range(self.count_elements):
            updated_queue[i] = self.queue[(self.head + i) % self.size]
        
        self.queue = updated_queue
        self.head = 0
        self.end = self.count_elements
        self.size = new_size
        print(f"Resized to {new_size} elements")

    def dequeue(self):
        # Last out and put new value there
        if self.count_elements == 0:
            return None  
        value = self.queue[self.head]
        self.head = (self.head + 1) % self.size
        self.count_elements -= 1
        self.tot -= value
        return value

    def enqueue(self, n):
        #Delete the first and add there
        if self.count_elements == self.size - 1:
            self.new_siz() 
        
        self.queue[self.end] = n
        self.end = (self.end + 1) % self.size
        self.count_elements += 1
        self.tot += n

    def avg(self):
       
        return self.tot / self.count_elements if self.count_elements > 0 else 0

    def count(self):
        
        return self.count_elements

   



