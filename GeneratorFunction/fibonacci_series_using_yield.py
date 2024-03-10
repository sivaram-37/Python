
def fib_series():
    a,b=0,1
    while(True):
        yield a
        a,b=b,a+b  

gen_fib=fib_series()
print(next(gen_fib))
print(next(gen_fib))

# or use for loop:

# first 5 terms of fibonacci series
for i in range(5):
    print(next(gen_fib))