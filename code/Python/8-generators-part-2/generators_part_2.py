# Creating a custom range data type
# Technically speaking, a Python generator must implement two
#  special dunder methods: __iter__() and __next__().
# Collectively, these are referred to a the iterator protocol.

class CustomRange():
    current = 0

    def __init__(self, first, last):
        print("\nHi from __init__")
        self.first = first
        self.last = last

    def __iter__(self):
        print("\nHi from __iter__\n")
        return self

    def __next__(self):
        print("Hi from __next__")
        if CustomRange.current < self.last:
            num = CustomRange.current
            CustomRange.current += 1
            return num
        raise StopIteration


rangeGen = CustomRange(0, 5)


def custom_for(iterable):
    print('before')
    iterator = iter(iterable)
    print('after')
    continueOn = True

    while continueOn:
        try:
            continueOn = False
            print('next(iterator)', next(iterator), '\n')
            continueOn = True
        except StopIteration:
            print("\nThat it.  We've reached the end of the line.")
            break


custom_for(rangeGen)
