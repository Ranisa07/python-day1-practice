"""
Pythoin List:
Features: 
i) Can contain duplicate items.
ii) Mutable: items cab be modified, replaced or removed.
iii) Ordered: maintains the order in which items are added.
iv) Index Based: items are accessed using their position(starting from 0)
v) can store mixed data types(integer, string, boolean, even othe lists)
"""
# Creating List:
# 1. Using Square Brackets
li = [1,2,3,34,4,45]
fruits = ["apple","banana","cherry"]
print(li)
print(fruits)

# 2. Using list() constructor:
li = list((1,2,3,'apple',4.5))
print(li)
li2 = list("GFG")
print(li2)

# 3. Creating list with repeated elements:
li = [2]*5
num = [0]*7
print(li)
print(num)
li_num = li + num  # Concatenate
print(li_num)

# Accessing List Elements:
li = [10,20,30,40,50,60,70]
print(li[0])
print(li[-1])
print(li[1:4])              # Elements from index 1 to 3
print(li[1:5:2])
print(li[::-1])             # Elements in reversed order

'''
append(): Adds an element at the end of the list
extend(): Adds multiple elements to the end of the list
insert(): Adds an element at a specific position
clear(): Removes all items
'''
# Example:
a = []
a.append(10)
print("After append(10):",a)

a.insert(0,5)
print("After insert(0,5):",a)

a.extend([15,38,29,33])
print("After extend[15,38,29,33]:",a)

a.clear()
print("After clear():",a)

a = [10,20,30,40,50]
a[1] = 25
print(a)

a.remove(30)
print("After remove(30):",a)

popped_val = a.pop(1)
print("Popped element:",popped_val)
print("After pop(1):",a)

del a[0]
print("After del a[0]:",a)

# Iterating Over Lists
a = ['apple','banana','cherry']
for item in a:
    print(item)

# Nested Lists:
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix[1][2])

# Sum of list
num = [10,20,30,40,50,60]
total = 0
for sum in num:
    total += sum
print(total)

# Largest Number:
li = [23,44,33,12,67,6]
largest = li[0]

for i in li:
    if largest < i:
        largest = i
print(largest)

# Count Even Numbers
li = [23,44,33,12,67,6]
count = 0
for num in li:
    if num % 2 == 0:
        count += 1
print(count)

# Smallest Number
li = [23,44,33,12,67,6,2]
smallest = li[0]
for num in li:
    if num < smallest:
        smallest = num
print(smallest)

# Reverse List
# Using append()
li = [23,44,33,12,67,6]
reversed_list = []
for i in range(len(li)-1,-1,-1):
    reversed_list.append(li[i])
print(reversed_list)

# Using insert()
li = [23,44,33,12,67,6]
reversed_list = []
for i in li:
    reversed_list.insert(0,i)
print(reversed_list)

# Using Slicing:
li = [23,44,33,12,67,6]
print(li[::-1])

# Using reverse() method:
li = [23,44,33,12,67,6]
li.reverse()
print(li)

# Add items in list from users
li = []
n=int(input("Enter length of list: "))
for i in range(0,n):
    num = int(input("Enter items: "))
    li.append(num)
    print(li)
print(li)


