import array as arr
a = arr.array('B',[34,76,89,54])    #typecode (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)
print(a[2])

a[3] = 45
print(a)    #array('B', [34, 76, 89, 45])

print("Inserting 67 at index 2")
a.insert(2,67)
print(a)
print("Removing 34")
a.remove(34)
print(a)
print("Appending....")
a.append(58)
a.append(92)
print(a)
print("Printing from range 0:3")
print(a[0:3])
