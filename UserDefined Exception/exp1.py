class InvalidAgeError(Exception):
    pass
def age(i):
    if i<18:
        raise InvalidAgeError
    else:
        print("Legal Age")
age(int(input()))