#!/usr/bin/env python
# coding: utf-8

# Q1.Implement Binary Search

# In[3]:


def binary_search(arr, a, low, high):

    while low <= high:

        mid = low + (high - low)//2

        if arr[mid] == a:
            return mid

        elif array[mid] < a:
            low = mid + 1

        else:
            high = mid - 1

    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8]
a = 4

print("The given array is", arr)


print("Element to be found is ", a)

index = binary_search(arr, a, 0, len(arr)-1)

if index != -1:
    print("The Index of the element is " + str(index))
else:
    print("Element Not found")


# Q2.Implement Merge Sort

# In[6]:


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              
              myList[k] = left[i]
             
              i += 1
            else:
                myList[k] = right[j]
                j += 1
           
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = [53,25,92,15,77,31,43,56,22]
mergeSort(myList)
print(myList)


# Q3.Implement Quick Sort

# In[ ]:


def quicksort(arr):

    if len(arr) <= 1:

        return arr

    else:

        pivot = arr[0]

        left = [x for x in arr[1:] if x < pivot]

        right = [x for x in arr[1:] if x >= pivot]

        return quicksort(left) + [pivot] + quicksort(right)

user_input = input("Enter the list of number: ")

arr = [int(x) for x in user_input.split()]

sorted_arr = quicksort(arr)

print("Sorted array:", sorted_arr)


# Q4.Implement Insertion Sort

# In[9]:





# Q5.Write a program to sort list of strings (similar to that of dictionary)

# In[3]:


lst = input('Enter the list for sorting').split()
 
lst.sort()
 
print('Sorted List: ' , lst)


# In[ ]:




