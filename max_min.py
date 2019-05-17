import random

lst = []
for i in range(1, 50):
    lst.append(random.randint(1, 200))
print(lst)
print('Greatest number is' , max(lst))
index1 = lst.index(max(lst))
print ('Index of max is ', index1)
print('Smallest number is' , min(lst))
index2 = lst.index(min(lst))
print ('Index of min is ' , index2)