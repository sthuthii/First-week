def problem3():
    test = int(input("Enter the number test cases"))
    if 1 <= test <=100:
        def check_scalene(a,b,c):
            if a!= b!= c:
                return True
        
        while test > 0: 
            print(" Enter values such that (a+b) > c")       
            x = int(input("A"))
            y = int(input("B"))
            z = int(input("C"))

            if z < (x+y):
                solution = check_scalene(x,y,z)
                if solution is True:
                    print("YES")
                else:
                    print("NO")    
            test -= 1        

    else:
        print("test cases should be between 1 and 100")  
        problem3()              
      

problem3()