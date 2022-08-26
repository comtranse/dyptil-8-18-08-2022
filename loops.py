li = [23,56,89,322,42]
for i in li:
    print(i)
for i in li:
    if(i==56):
        print("Found")
print("Use of continue")
li2 = [5,6,7,8,9]
for i in li2:
    if i==6:
        continue
    print(i)

#Task-5 
#To find prime number
# print("Prime number from 2 to 10")
# for i in range(2,11):
#     count=0
#     for j in range(2,i):
#         if(i%j)==0:
#             count = count + 1
#     if count == 0:
#         print(i)
#     else:
#         count=0
print("Prime numbers from 2 to 10")
for p in range(2,11):
    for n in range(2,p):
        if(p%n==0):
            break
    else:
        print(p)
