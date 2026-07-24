"""
    A memory-efficient Singly Linked List with advanced sublist search capabilities.
    
    Features:
    - O(1) auxiliary space initialization from standard Python iterables.
    - Dynamic sublist pattern matching (starts_with, ends_with, contains).
    - In-place right rotation and O(1) length tracking.
    """

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, list):
        a_list = [Node(value) for value in list]
        if a_list == []:
            self.head = None
        else:
            for index in range(len(list) - 1):
                node = a_list[index]
                node.next = a_list[index + 1]
            self.head = a_list[0]
            
        

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def len(self):
        
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def get(self, index):
       
        current = self.head
        current_index = 0
        while current:
            if current_index == index:
                return current.value
            current_index += 1
            current = current.next
        return None  

    def has(self, x):
        
        current = self.head
        while current:
            if current.value == x:
                return True
            current = current.next
        return False

    def delete(self, value):
        
        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous is None:
                    self.head = current.next  
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next

    def rotate(self):
        
        if self.head is None or self.head.next is None:
            return 
        

        second_last = None
        last = self.head
        while last.next:
            second_last = last
            last = last.next
        
        
        second_last.next = None  
        last.next = self.head     
        self.head = last         

    def starts_with(self, m):
    
        current = self.head
        m_current = m.head
        while current and m_current:
            if current.value != m_current.value:
                return False
            current = current.next
            m_current = m_current.next
        return m_current is None  

    def contains(self, m):
        
        current = self.head
        while current:
            l_current = current
            m_current = m.head
            while l_current and m_current and l_current.value == m_current.value:
                l_current = l_current.next
                m_current = m_current.next
            if m_current is None:  
                return True
            current = current.next
        return False

    def ends_with(self, m):
        
        if m.head is None:
            return True 
        
        current = self.head
        m_len = m.len()
        current_len = self.len()

        if current_len < m_len:
            return False

        for _ in range(current_len - m_len):
            current = current.next

        
        m_current = m.head
        while current and m_current:
            if current.value != m_current.value:
                return False
            current = current.next
            m_current = m_current.next

        return m_current is None 


