table_ip = int(input("enter the number to write their table"))

for i in range(1,table_ip):
    if i > 10 :
        break
    print(table_ip," * " , i , " = ", i*table_ip)
