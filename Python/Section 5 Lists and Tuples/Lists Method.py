l1 = [2,6,5,3,1,9,8,10,12]
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.append(22)
print(l1)
l1.insert(0,22)
print(l1)
l2 = [2,4,6,7,8,9,10]
l1.extend(l2)
print(l1)
l3 = l1+l2
print("l3 ",l3)

my_list = [1,2,3,4,5]
my_list.remove(1)
print(my_list)

del my_list[2]
print(my_list)

