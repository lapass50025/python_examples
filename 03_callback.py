def sum(a, b):
    print("{0} + {1} = {2}".format(a, b, a+b))

def exp(a):
    print("{}".format(a**2))

def callfunc(callfn, call_args=()):
    if callfn != None:
        callfn(*call_args)

callfunc(sum, call_args=(1, 2))
callfunc(exp, call_args=(2,))
