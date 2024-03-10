def play():
    yield 100
    yield 200

score=play()
print(score)
print(next(score))
print(next(score))
# print(next(score)) --> Error : StopIteration