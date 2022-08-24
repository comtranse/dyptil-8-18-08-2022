list=[12,14,15,78j,"mno","pqr",[789,"demo"],(65,67)]
print(list)

#TO insert
list.insert(2,33)
print(list)
#to append
list.append(47)
print(list)

list[4]="ppp"
print(list)


list.remove(15)
print(list)
#pop
list.pop(4)
print(list)
list.clear()
print(list)
del(list)
print(list)