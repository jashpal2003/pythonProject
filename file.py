f1 = open("new.txt","r")
file_content = f1.read()
print(file_content)

f2 = open("new.txt","w")
f2.write("good morning ")

f3= open("new.txt","r")
file_content = f3.read()
print(file_content)


