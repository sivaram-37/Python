def div(a,b):
    try:
        print("Division = ",a/b)
    except ZeroDivisionError:
        print("ZeroDivisionError Exception Handled..!!!")
    except NameError:
        print("NameError Exception Handled..!!!")
    except TypeError:
        print("TypeError Exception Handled..!!!")
    except:
        print("some exception handled..!!!")
        
div(int(input('''Enter the value for 'a' =''')),int(input('''Enter the value for 'b' =''')))
