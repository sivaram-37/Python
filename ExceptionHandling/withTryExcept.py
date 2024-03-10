def div(a,b):
    try:
        print("Division = ",a/b)
    except:
        print("Exception Handled")
        
div(int(input('''Enter the value for 'a' =''')),int(input('''Enter the value for 'b' =''')))
