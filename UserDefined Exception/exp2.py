class InvalidPinError(Exception):
    pass

def check():
    pin=int(input("Enter the PIN Number : "))
    if pin==1927:
        print("Valid PIN, Withdraw the money")
    else:
        raise InvalidPinError
try:
    check()
except:
    print("Invalid PIN, Two attempt are remaining..!!!")
    
    try:
        check()
    except:
        print("Invalid PIN, One attempt is remaining..!!!")
        
        try:
            check()
        except:
            print("Invalid PIN, Your account is blocked..!!!")