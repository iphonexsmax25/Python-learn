num = int(input("Enter Number: "))
n = 2
while n < num:
    rem =  num % n
    if rem == 0:
        print("No")
        break
    else:
        n += 1


if n == num:
    print("Yes")