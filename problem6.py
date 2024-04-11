num = int(input("Enter a number"))
number = 0

while num!=0:
    if num%2 == 0:
        num = num/2
    else:
        num = num - 1

    number = number + 1   

print(number)