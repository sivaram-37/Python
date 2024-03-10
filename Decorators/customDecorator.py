def decor(function):
    def inner(name):
        if name=="Ram":
            print(name,"likes Pasta")
        else:
            function(name)
    return inner

@decor
def food(name):
    print(name,"likes Biryani")
food("Siva")
food("Ram")
food("Suganya")
