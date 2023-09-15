#!/usr/bin/env python
# coding: utf-8

# Q1.Delete the elements in an linked list whose sum is equal to zero

class Node():
  def __init__(self,data):
     self.data = data
     self.next = None

class Linkedlist():
   def __init__(self):
     self.head = None
    
   def append(self,data):
     new_node = Node(data)
     h = self.head
     if self.head is None:
         self.head = new_node
         return
     else:
         while h.next!=None:
             h = h.next
         h.next = new_node

   def remove_zeros_from_linkedlist(self, head):
     stack = []
     curr = head
     list = []
     while (curr):
         if curr.data >= 0:
             stack.append(curr)
         else:
             temp = curr
             sum = temp.data
             flag = False
             while (len(stack) != 0):
                 temp2 = stack.pop()
                 sum += temp2.data
                 if sum == 0:
                     flag = True
                     list = []
                     break
                 elif sum > 0:
                     list.append(temp2)
             if not flag:
                 if len(list) > 0:
                     for i in range(len(list)):
                         stack.append(list.pop())
                 stack.append(temp)
         curr = curr.next
     return [i.data for i in stack]

if __name__ == "__main__":
 l = Linkedlist()

 l.append(4)
 l.append(6)
 l.append(-10)
 l.append(8)
 l.append(9)
 l.append(10)
 l.append(-19)
 l.append(10)
 l.append(-18)
 l.append(20)
 l.append(25)
 print(l.remove_zeros_from_linkedlist(l.head))





# Q2.Reverse a linked list in groups of given size

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  
class LinkedList:
    def __init__(self):
        self.head = None
  
    def reverse(self, head, k):
        
        if head == None:
          return None
        current = head
        next = None
        prev = None
        count = 0

        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
  
        if next is not None:
            head.next = self.reverse(next, k)

        return prev
  
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
  

llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
  
print("Given linked list")
llist.printList()
llist.head = llist.reverse(llist.head, 3)
  
print ("\nReversed Linked list")
llist.printList()





# Q3.Merge a linked list into another linked list at alternate positions.

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
def printList(msg, head):
 
    print(msg, end='')
 
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
 
    print('None')
 
def shuffleMerge(a, b):
 
    dummy = Node()
    tail = dummy
 
    while True:
        if a is None:
            tail.next = b
            break
 
        elif b is None:
            tail.next = a
            break
 
        else:
            tail.next = a
            tail = a
            a = a.next
 
            tail.next = b
            tail = b
            b = b.next
 
    return dummy.next
 
 
if __name__ == '__main__':
 
    a = b = None
    for i in reversed(range(1, 8, 2)):
        a = Node(i, a)
 
    for i in reversed(range(2, 7, 2)):
        b = Node(i, b)
 
    printList('First List: ', a)
    printList('Second List: ', b)
 
    head = shuffleMerge(a, b)
    printList('After Merge: ', head)





# Q4.In an array, Count Pairs with given sum

def getPairsCount(arr, n, sum):
    unordered_map = {}
    count = 0
    for i in range(n):
        if sum - arr[i] in unordered_map:
            count += unordered_map[sum - arr[i]]
        if arr[i] in unordered_map:
            unordered_map[arr[i]] += 1
        else:
            unordered_map[arr[i]] = 1
    return count
arr = [1, 5, 7, -1]
n = len(arr)
sum = 6
print('Count of pairs is', getPairsCount(arr, n, sum))





# Q5.Find duplicates in an array

def find(array):
    duplicate_element_array = []
    for i in array:
        if array.count(i) > 1 and i not in duplicate_element_array:
            duplicate_element_array.append(i)
    print("Duplicate element in an array : ", end="")
    for i in sorted(duplicate_element_array):
        print(i, end=" ")

array = [-1, 8, 1, 8, -1, 5, 1, -3]
print("Array= ", array)
find(array)




# Q6.Find the Kth largest and Kth smallest number in an array

def heaping (array, n, k):
    greatest = k 
    left = 2*k + 1
    
    right = 2*k + 2
    
    if left < n and array[k] < array[left]:
        greatest = left
    
    if right < n and array[greatest] < array[right]:
        greatest = right
    if greatest != k :
        array[greatest],array[k] = array[k],array[greatest]

def max_heap(array,n): 

    for i in range(n, -1, -1): 
        heaping(array, n, i)   
    for num in range(n-1, -1, -1): 
        array[num], array[0] = array[0], array[num] 
        heaping(array,num, 0) 
array = [ 12, 11, 13, 5, 6, 7] 
n = len(array)
max_heap(array, n) 
k = 3
print(array[k-1]) 
print(array[-k])


#Q7.Move all the negative elements to one side of the array

def find(arr):
    ans = []
    for i in arr:
        if i < 0:
            ans.append(i)
        if 0 in arr:
            ans.append(0)
    for i in arr:
        if i > 0:
            ans.append(i)
    ans = ans[::-1]

    print("Array after moving all the elements to right:", ans)
array = [1, 3, -1, 4, -3, -5, -6, 3, 7]
find(array)


#Q8.Reverse a string using a stack data structure

class  Stack_to_reverse  :
    
    def __init__(  self  ):
        self.items  =  list()
        self.size=-1
    def  isEmpty(  self  ):
        if(self.size==-1):
            return True
        else:
            return False
 
    def  pop(  self  ):
        if  self.isEmpty():
            print("Stack is empty")
        else:
            return self.items.pop()
            self.size-=1
    def  push(  self,  item  ):
        self.items.append(item)
        self.size+=1
 
    def reverse(self,string):
        n = len(string)
 
        for i in range(0,n):
            S.push(string[i])
 
        string=""
 
        for i in range(0,n):
            string+=S.pop()
        return string
 
S=Stack_to_reverse()
seq=input("Enter a string to be reversed: ")
sequence = S.reverse(seq)
print("Reversed string is: " + sequence)



# Q9.Evaluate a postfix expression using stack.

def evaluate_postfix(postfix_expr):
    stack = []
    operators = set(['+', '-', '*', '/', '%', '^'])
    
    for elem in postfix_expr:
        if elem not in operators:
            stack.append(float(elem))
        else:
            b = stack.pop()
            a = stack.pop()
            if elem == '+':
                stack.append(a + b)
            elif elem == '-':
                stack.append(a - b)
            elif elem == '*':
                stack.append(a * b)
            elif elem == '/':
                stack.append(a / b)
            elif elem == '%':
                stack.append(a % b)
            elif elem == '^':
                stack.append(a ** b)
                
    return stack.pop()
postfix = '236*+' 
evaluate_postfix(postfix)
print('{} \t: {}'.format(postfix, evaluate_postfix(postfix)))
postfix = '23*6+' 
evaluate_postfix(postfix)
print('{} \t: {}'.format(postfix, evaluate_postfix(postfix)))
postfix = '23*42/+'  
evaluate_postfix(postfix)
print('{} : {}'.format(postfix, evaluate_postfix(postfix)))


# Q10.Implement a queue using the stack data structure.

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
 
    def enQueue(self, x):
        self.s1.append(x)
 
    def deQueue(self):
 
        if len(self.s1) == 0 and len(self.s2) == 0:
            return -1
 
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1):
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()
 
        else:
            return self.s2.pop()

if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
 
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
