def gen_func(num):
    for i in [7, 8, 9]:
        print(i)
        yield i


# This is how a for loop works underneath the hood
def special_for(iterable):
    print('iterable:', iterable)
    iterator = iter(iterable)
    print('iterator:', iterator)
    while True:
        try:
            print('next(iterator)', next(iterator))

        except StopIteration:
            print("We're done here.  See you later!\n")
            break


special_for(gen_func(3))
