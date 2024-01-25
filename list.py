l1 = [1,2,3,4,5,6,'jashpal']
l2 = [4,5,6,7,8,9,"india"]
print(l1[:2])
print(l1[:])
l1.append("iron man")
print(l1)
l1.extend(l2)
print(l1)
l1.insert(3,"insert at 4thrd position")
print(l1)
l1[3] = "moye moye"
print(l1)
del l1[2]
print(l1)
print("moye moye" in l1)