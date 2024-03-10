def alpha():
    try:
        print("Connection of alpha established")
        a=10
        b=0
        print(a/b)
        print("Connection of alpha ended")
    except:
        print("Exception Handled..!!!")
def beta():
    print("Connection of beta established")
    alpha()
    print("Connection of beta ended")
def gamma():
    print("Connection of gamma established")
    beta()
    print("Connection of gamma ended")
gamma()