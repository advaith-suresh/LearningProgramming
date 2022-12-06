#Learning Python

In this file I wil try to write down the interesting things I come across while learning python

1. Functions can be passed as arguments, and also can be returned!
    def inc(x):
        return x + 1

    def dec(x):
        return x - 1

    def operate(func, x):
        result = func(x)
        return result
   Here operate is a higher order function

2. there are no inbuild private variables to a class just convention _private (this disturbs me deeply coming from c++)

3. closure: interpretor remembers values of variables that are just outside the scope of the nested function even after the parent function has finished
    def print_msg(msg):
        # This is the outer enclosing function
        def printer():
            # This is the nested function
            print(msg)
        return printer  # returns the nested function
    
    another = print_msg("Hello")
    another()
    # Output: Hello

    Used in decorators

