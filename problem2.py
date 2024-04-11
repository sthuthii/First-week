test = int(input("Enter the number of test cases"))



def number_of_chocolates(x,y,z):
    cost = x*5 + y*10
    choco = int(cost/z)
    return choco

while test > 0:
    a = int(input("Enter the number of 5 rupee coins"))
    b = int(input("Enter the number of 10 rupee coins"))
    c = int(input("Enter the cost of each chocolate"))

    solution = number_of_chocolates(a,b,c)
    print(f"Hence the number of chocolates are {solution}")
    test -= 1


