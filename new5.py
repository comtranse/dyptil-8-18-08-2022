from os import remove
from tkinter import SE
from typing import Set


Set={1,5.0,"soham"}
print(Set)
Set.add(60)
# print(Set)
Set.remove("soham")
print(Set)
Set2={25,56,23,45}
print(Set.intersection_update(Set2))
print(Set.symmetric_difference(Set2))
dict={1:"hi",2:"hello"}
print(dict)
print(dict[1])
print(dict[2])
print(dict.keys)
# print(dict.items())
dict[3]="nice"
print(dict.items())
dict.update({4:"good"})
print(dict.items())
dict.update({3:"apple"})
print(dict.items())
# dict.pop()
# print(dict)
for i in range(1,4):
    print(dict)
dict2={5:"ice",6:"spice",7:"ink"}
object={"var1":dict,"var2":dict2}
print(object)
