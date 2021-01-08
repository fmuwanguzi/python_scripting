from functools import lru_cache

@lru_cache(maxsize = 100)
def fibonacci(n):
    #edge case
    #check that the interger is a positive number
    if type(n) != int:
        raise TypeError('Value must be a positive number')
    if n <  1:
        raise ValueError('Number needs to be positive')
    
    #base case
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        # recursive step
        return fibonacci(n-1) + fibonacci(n-2)
    
#print(fibonacci('seven'))
#print(fibonacci(-10))   
# print(fibonacci(5))

for n in range(1, 100):
    print(n, ':', fibonacci(n))


#solution with memorization this makes the above problem faster  
# fib_cache = {}
# def fibonacci(n):
#     """if we have cached the value already then we can just return it"""
#     if n in fib_cache:
#         return fib_cache[n]
        
#     #Compute the nth term
#     if n == 1:
#         value = 1
#     elif n == 2:
#         value = 1
#     elif n > 2:
#         value = fibonacci(n-1) + fibonacci(n-2)
        
#     #cache the value and return it
#     fib_cache[n] = value
#     return value

# for n in range(1, 100):
#     print(n, ':', fibonacci(n))