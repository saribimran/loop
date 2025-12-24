num = int(input("Enter a number: "))
c=0

while num:
    c+=1
    num//=10

    print(c)