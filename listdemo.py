
alist = [12,14,16.5,"abc","pqr",(34,85)]
print(alist)

#To insert
alist.insert(2,33)
print(alist)

#To append
alist.append(47)
print(alist)

alist[5] = "jkl"
print(alist)

#To remove
alist.remove(16.5)          #To remove particular element
print(alist)

alist.pop(4)                #To delete element at a particular index
print(alist)

alist.clear()
print(alist)
# del(alist)
# print(alist)


list2 = [12,14,16.5,"abc","pqr",(34,85)]
print(list2[0:4])