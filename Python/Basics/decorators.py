# basic example
'''
def premultiply(func):
    def inner(a, b):
        print("this is the decorated")
        func(a,b)
    return inner

@premultiply
def bode(a,b):
    print(f"hi I'm here {a} {b}")

bode(1,2)
'''

# using @property        

class Watch:
    def __init__(self, time):
        self.time = time
        
    def set_time(self, time):
        print("Okay okay I'll set the time")
        self._time = time
    
    
    def get_time(self):
        return self._time

    time = property(get_time, set_time)

rolex = Watch(6)



# INCOMPLETE: recreating @property
# how to see if 'time' is on left side of equality or right?
'''
def ownthing(func1, func2): # ownthing == property
    def inner(time):

'''