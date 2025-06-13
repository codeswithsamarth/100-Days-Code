# Set is a collection of unordered non repetative elements unindexed

sets = set()
print(sets)

s1 =  {1,1,2,3,4,5,6,7,8,9}
print(s1)

s1.add(99)
print(s1)

s1.remove(99)
print(s1)

a = s1.pop()
print(s1)

sd = {1,2,3,4}
sd.discard(3)
print(sd)

s1 = {1,2,3}
s2 = {4,5,6}
print(s1.union(s2))

# intersection returns commmon elements

s1 = {1,2,3}
s2 = {3,2,5}
print(s1.intersection(s2))

# difference returns the different elements present in current set

s1= {1,2,3,4}
s2 = {2,4,6}

print(s2.difference(s1))

s1 = {11,22,33,44}
s2 = {22,44,66,88}

print(s2.difference(s1))

sd = {1,2,3}
sd2 = {2,4,6}
print(sd.symmetric_difference(sd2))

sb1 = {1,2,3,4,5,6}
sb2 = {2,4,6}

print(sb1.issuperset(sb2))

a = {1,2}
b = {3,5}
print(a.isdisjoint(b))

