def closest_pivot_number(n):
    total_sum = n * (n+1)//2
    left_sum =0
    right_sum = total_sum
    pivot = 1
    min_diff = float('inf')


    for i in range(1,n):
        left_sum += i
        right_sum -= i
        diff = abs(left_sum - right_sum)

        if diff < min_diff:
            min_diff = diff
            pivot = i+1

    return pivot

while True:
    try:
      n = int(input("Enter a positive number"))
      if n <=0:
          raise ValueError("Please enter a positive natural number")
      break
    except ValueError as e:
        print(e)

pivot = closest_pivot_number(n)
print(f"Pivot number is {pivot}")            


