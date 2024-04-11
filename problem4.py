test = int(input("Enter the number of test cases"))
if 1 <= test <=100:
    
    solution = 0


    while test > 0:
        number = int(input("Enter a number btween 1 and 1000"))
        if number%2 ==0 and number%7 == 0:
            solution = 1
        elif number%2 !=0 and number%9 == 0:
            solution = 2
        else:
            solution = 3
        test -= 1   
        if solution == 1:
           print("Alice")        
        elif solution == 2:
            print("Bob")
        else:
            print("Charlie")    