def div(a,b):
    try:
        c=a/b
    except:
        print("Exception Handled..!!!")
    else:
        print("Else Block Executed..!!! >>> The Division = {c}")
    finally:
        print("Finally Block Executed..!!!")

div(int(input('''Enter the value for 'a'=''')),int(input('''Enter the value for 'b'=''')))