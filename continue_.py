ip = int(input("input number where to stop"))
ip_2 = int(input("enter the number that need to skip we skip there multiply"))
i = 1
while ip >= i:
    if i % ip_2 == 0:
        i+=1
        continue
    if i == ip :
        print("exit")
        break
    print(i)
    i+=1
