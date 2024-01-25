import struct

n = [1,2,3,4,5,6,7]
print(list(map(lambda x:x**2,n)))
print([x**2 for x in n])


word = ["jashpal","iron-man","batman","thor","loki"]
uper_case= list(map(str.upper,word))
print(uper_case)


wo = ["jashpal","iron-man","batman","thor","loki"]
w_len = list(map(len,wo))
print(w_len)