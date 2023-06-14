some_numbers = [1, 2, 3]
a = 20

def add(x,y):
    return x+y

class Something:
    pass


if (__name__ == '__main__'):
    print(f"Root Number = {a}")
    print(f"Number List = {some_numbers}")
    print(f"Adding both = {[add(a, number) for number in some_numbers]}")
    
