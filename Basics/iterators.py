'''
Learning: some properties of Iterators and iterables, and Generators
'''

class Queue:
    def __init__(self):
        self.n = 0

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        self.n += 1
        if self.n <= 20:
            return self.n
        else:
            raise StopIteration

shop = Queue()

# making a loop using iterators
'''
line = shop.__iter__()

while 1:
    try:
        print(line.__next__())
    except StopIteration:
        print("Have to stop here sorry :(")
        break
'''

# making 2 iterator objects to see how they interact
# ans: since line 2 is still SHOP the __iter__ command brings n of SHOP to 0, which brings n of LINE1 to 0
'''
line1 = shop.__iter__()
print(line1.__next__())
print(line1.__next__())

line2 = shop.__iter__()
print(line1.__next__())
print(line1.__next__())
'''

# do we even need iter
# ans: not if we use it like below
'''
while 1:
    try:
        print(shop.__next__())
    except StopIteration:
        print("Have to stop here sorry :(")
        break
'''

# to use the class as an iterable like below we need the __iter__ method
# else TypeError: 'Queue' object is not iterable
'''
for i in shop:
    print(i)
'''

# working with Generators
'''
def gen():
    n = 0
    while 1:
        n += 2
        yield n

gen_obj = gen()

i = 0
while i < 10:
    print(next(gen_obj))
    i += 1
'''