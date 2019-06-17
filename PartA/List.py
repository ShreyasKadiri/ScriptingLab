from functools import reduce

list1=[134,22,43,34,25,26]
print("Original",list1)
list2=[x*3 for x in list1]
print("New",list2)

or_sum = reduce(lambda x,y: x+y,list1)
print("Original sum",or_sum)

new_sum = reduce(lambda x,y: x+y,list1)
print("New sum",new_sum)
