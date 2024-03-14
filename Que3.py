numbers = [5, -8, 12, -3, 17, 0, -10, 6]

positive_sq = [num**2 for num in numbers if num > 0]

negative_cub = [num**3 for num in numbers if num < 0]

absolute_val = [abs(num) for num in numbers]

even_num = [num for num in numbers if num % 2 == 0 and num >= 10]

print("Squares of positive integers:", positive_sq)
print("Cubes of negative integers:", negative_cub)
print("Absolute values of all integers:", absolute_val)
print("Even numbers Greater than 12:", even_num)
