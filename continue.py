print("\t\t ******* clap on division ******* \t\t")

ip = input("enter the number to which you skipping for ram game")
i = 1
while 1:
    ip_1 = input("enter your number player no 1 ")
    if ip.isalpha():
        if ip%i == 0:
            continue
        else:
            print("you enter wrong clap")
            break
    if ip_1 == i :
        if ip_1 % ip == 0:
            print("you enter the number when you need to write clap")
            break
    else:
        print("s1")
        print("wrong order ")
        print("i",i,"ip_1",ip_1,"ip",ip)
    i+=1
    ip_2 = input("enter your number player no 2 ")
    if ip.isalpha():
        if ip%i == 0:
            continue
        else:
            print("s2")
            print("you enter wrong clap")
            break
    if ip_2 == i :
        if ip_2 % ip == 0:
            print("you enter the number when you need to write clap")
            break
    else:
        print("wrong order bro")
    i += 1
