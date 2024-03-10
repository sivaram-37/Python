def divCheck(function):
    def inner(a,b):
        if b==0:
            print("B cannot be zero")
        else:
            function(a,b)
    return inner
 

@divCheck
def div(a,b):
    print(a/b)

div(20,10)
div(10,0)