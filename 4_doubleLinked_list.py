class DoubleLinkedList :
    def __init__(self,value):
        new_node = Node(value)
        self.next=self.tail
        self.previous=self.head
        self.length+=1
        return new_node
    
    def append(self,value):
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            new_node.previous = self.tail
            self.tail = new_node
            self.length +=1        
        return True
    
    def pop(self):
        if self.length == 0:
            return None 
        else:
            self.tail = self.tail.previous
            self.tail.next = None


        self.tail.next = self.tail.previous



        



    
class Node :
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


