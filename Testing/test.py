
integer = [1,2,3,4,5,6,7,8,9,10]
odd = [n for n in integer if n%2==1]
even = [n for n in integer if n%2==0]


# decorator + list comprehension example
def Even(func):
    def wrapper():
        print(" ".join(str(item) for item in even))
        func()
    return wrapper

@Even
def Odd():
    print(" ".join(str(item) for item in odd))
