no = {2,2,3,4,5,6,7,8,9,}
print(no)

e_set = set()
print(type(e_set))
e_set.add(1)
print(e_set)

for i in no:
    print(i)
print(no.union(e_set))
print(no.intersection(e_set))
print(no.difference(e_set))
print(no.symmetric_difference(e_set))