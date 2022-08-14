#def head = {
#        
#                "value" : 1,
#                "next"  :{
#                            'value' :2,
#                            'next'  :{
#                                        'value' :3
#                                        'next'  :{
#                                                    value : 4,
#                                                    next : None
#                                                }
#                                    }
#
#                        }
#    }

from http.client import NotConnected
from operator import truediv


class LinkedList :
     def __init__(self, value):
        new_node = Node(value)   
        self.head = new_node
        self.tail = new_node
        self.length = 1

     def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
     def append(self, value):
         new_node = Node(value)
         if self.length == 0:
             self.head = new_node
             self.tail = new_node
         else:
             self.tail.next = new_node   #TAIL is the last node itself
             self.tail = new_node
         self.length +=1
             
     def prepend(self, value):
         new_node = Node(value)
         new_node.next = self.head
         self.head = new_node
         
         if self.length == 0:
             self.tail = new_node
         self.length +=1

     def pop(self):
         temp = self.head
         pre_temp = self.head
         
         if self.head == None:
            return None
         while (temp.next):
          pre_temp = temp
          temp = temp.next
        
         pre_temp.next = None
         self.tail = pre_temp
         self.length -=1

         if self.length == None:    # for 1 item in ll
             self.head = None
             self.tail = None  
         return temp.value
    
     def pop_first(self):
         if self.length == 0:
             return None

         temp = self.head
         self.head = self.head.next
         temp.next = None
         self.length -=1

         if self.length == 0:
             self.tail = None

     def get(self, index):
         if index <=-1 or index> self.length:
             return None
         if self.length ==0:
            return None

         temp = self.head
         for _ in range (index):
             temp = temp.next
             return temp
    
     def set(self, index, value):
         temp = self.get(index)
         if temp:
            temp.value = value
            return True
         return False



class Node :
    def __init__(self, value):
        self.value = value
        self.next = None

print('LL created')
my_linked_list = LinkedList(3) 
my_linked_list.printList()    
print('append called')
my_linked_list.append(4)
my_linked_list.printList()
print('prepend called')    
my_linked_list.prepend(2)
my_linked_list.printList()
print('pop called')    
my_linked_list.pop()
my_linked_list.printList()
print('pop first called')    
my_linked_list.pop_first()
my_linked_list.printList()


