#Learning Python

In this file I wil try to write down the interesting things I come across while learning python

1. Functions can be passed as arguments!
    def inc(x):
        return x + 1

    def dec(x):
        return x - 1

    def operate(func, x):
        result = func(x)
        return result

2. there are no inbuild private variables to a class just convention _private
