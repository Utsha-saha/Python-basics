#!/usr/bin/env python
# coding: utf-8

# In[1]:


tup1 = (1, 2, "a")
tup1


# In[2]:


tup1[0]


# In[3]:


dict1 = {'mango': 1, 'apple': 2}
dict1


# In[4]:


dict1.keys()


# In[6]:


dict1.values()


# In[13]:


#array
arr = []
len1=input()
len1=int(len1)
for i in range(len1):
    element=input()
    arr.append(element)
for i in range(len1):
    print(arr[i])


# In[20]:


row=int(input("enter the row number"))
col=int(input("enter the col number"))

two_d_arr = [[0 for i in range(col)]for j in range(row)]
print("Two D arrays are:")
for i in range(row):
    for j in range(col):
        two_d_arr[i][j] = i*j
print(two_d_arr)
        


# In[23]:


#implementation of stack with queue
from queue import LifoQueue
stack=LifoQueue(maxsize=3)
stack.put(5)
stack.put(9)
stack.put(10)
print(stack.qsize())
print(stack.full())


# In[24]:


stack.get()


# In[25]:


print(stack.full())


# In[29]:


class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue)<1:
            return None
        self.queue.pop()
    def display(self):
        print(self.queue)
q=Queue()
q.enqueue(5)
q.enqueue(9) 
q.dequeue()
q.display()


# In[30]:


#Linked List
#Node creation
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
n1 = Node(8)


# In[31]:


n2 = Node(3)
print(n1.data)
print(n1.next)


# In[62]:


#Insertion at beginning of Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Llf:
    def __init__(self):
        self.head = None
        
    def traversal(self):
        if self.head is None:
            print("List empty")
        else:
            a=self.head
            while a is not None:
                print(a.data)
                a=a.next
                
    def insertion_at_beginning(self,data): 
        print()
        newdata = Node(data) #object of class Node
        newdata.next = self.head
        self.head = newdata
        
    def insertion_at_end(self,data2):
        newdata2 = Node(data2)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = newdata2
        
    def insertion_at_any_pos(self,position,data):
        print()
        newdata3 = Node(data)
        a = self.head #newdata
        for i in range(1,position - 1): #only for i=1
            a = a.next #a = a.next = n1
        newdata3.next = a.next #a.next = n1.next = n2
        a.next = newdata3 #a.next = n2 = now inserted
    def deletion_at_beg(self):
        print()
        a = self.head
        self.head = a.next #n1
        a.next = None
    def deletion_at_end(self):
        print()
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None
    def delete_any_pos(self,pos):
        print()
        prev = self.head
        a = self.head.next
        for i in range(1,pos-1):
            a = a.next
            prev = prev.next
        prev.next = a.next
        a.next = None
                                    
        
n1 = Node(5)
llf = Llf()
llf.head = n1
n2 = Node(9)
n1.next = n2
n3 = Node(10)
n2.next = n3
llf.traversal()
llf.insertion_at_beginning(91)
llf.traversal()
llf.insertion_at_end(99)
llf.traversal()
llf.insertion_at_any_pos(2,7)
llf.traversal()
llf.deletion_at_beg()
llf.traversal()
llf.deletion_at_end()
llf.traversal()
llf.delete_any_pos(3)
llf.traversal()
            


# In[50]:


import os

class FOO():
    def __init__(self):
        self.values = [2, 4, 6, 8]

    def do_something(self, x, y):
        os.system("clear")
        z = self.values[x] * self.values[y]
        print( "%r * %r = %r" % (self.values[x], self.values[y], z))


class BAR():
    def __init__(self):
        self.foo1 = FOO()

    def something_else(self, a, b):
        self.foo1.do_something(a, b)

bar = BAR()
bar.something_else(1, 2)


# In[ ]:




