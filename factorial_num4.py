def factorial(num):
    if num <= 1:
        yield 1
    else:
        yield num * fact1(num - 1)

for i in range(5):
    if(factorial(i)):
        print(i)

# def factorial(num):
#     if num <= 1:
#         return 1
#     else:
#         return num * factorial( num - 1)

# for i in range(3):
#     if(factorial(i)):
#         print((i))
