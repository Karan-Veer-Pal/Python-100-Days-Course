# Day : 23 List Methods

#append():
# This method appends items to the end of the existing list.
l = [1, 2, 3, 4]
print(l)
l.append(7) # add 7 in last
print(l)

print("\n")

#sort():
# This method sorts the list in ascending order. The original list is updated
e = [11, 45, 1, 5, 4, 2, 6]
print(e)
e.sort()
print(e)

print("\n")

#sort in reverse
a = [11, 45, 1, 5, 4, 2, 6]
print(a)
a.sort(reverse = True)
print(a)

print("\n")

#reverse():
# This method reverses the order of the list.
b = [11, 45, 1, 5, 4, 2, 6]
print(b)
b.reverse() # print list in reverse order
print(b)

print("\n")

#Fetch value from a give index
# This method returns the index of the first occurrence of the list item.
c = [11, 45, 1, 2, 4, 6, 3]
print(c)
print(c.index(1)) # return the value on index 1

print("\n")

#count the occurance of a given number in a list
# Returns the count of the number of items with the given value.
d = [11, 45, 1, 2, 4, 2, 6, 2, 3, 2]
print(d)
print(d.count(2))

print("\n")

# when we do a change in a list then it will also reflect the change in another list when they a connected
f = [11, 45, 1, 2, 4, 6, 1, 2]
print(f)
m = f
m[0] = 0
print(f)

print("\n")

# to overcome this problem we use copy() function
# Returns copy of the list. This can be done to perform operations on the list without modifying the original list.
g = [11, 45, 1, 2, 4, 6, 1, 2]
print(g)
m = g.copy()
m[0] = 0
print(g)

print("\n")

#insert():
# This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.
h = [11, 45, 1, 2, 3, 4, 5, 6]
print(h)
h.insert(1, 889) # 1 index per 889 print kardo
print(h)

print("\n")

#extend():
# This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
j = [11, 45, 1, 2, 3, 4, 5, 6]
i = [900, 1000, 1100]
i.extend(j) #means open i and place in h after end
print(i)

print("\n")

# concatenating two lists:
# You can simply concatenate two lists to join two lists.
x = [1, 2, 3, 4, 5]
y = [98, 99, 100]
z = x + y
print(z)
