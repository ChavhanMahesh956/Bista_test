def factorial(num):
    if num <= 1:
        yield 1
    
    for i in range(num):
            yield (i * factorial(i - 1))
    yield num

for i in range(5):
    print(factorial(i))

# def factorial(num):
#     if num <= 1:
#         return 1
#     for i in range(0, num):
#         return i * factorial( i - 1)
#     return i
    
# print(factorial(10))
