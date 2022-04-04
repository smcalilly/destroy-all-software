# halting problem

# will function f termintate when we call it or will it loop forever?
def halt(f):
    pass

def hatler():
    return


def looper():
    while True:
        pass

# halts(halter) => True
# halts(looper) => False

def impossible():
    return halts(impossible) and looper()

# assume impossible halts (returns True)
    # call itself inside and it doesn't halt
# assume impossible doesn't halt (returns False)
    # call it and the right hand side won't evaluate
    # which means it did termintate

# proof by contradiction
#  assumed the thing we wanted to disprove was true and showed that it led to a contradiction, so it must be False

# more examples

# COMPILERS
1 + 2 + x
# optimize into because those are constants
3 + x

# return a constant
def f():
    return 1 + 2 + 3

# what about when function returns constant?
# this is an undecidable problem
def returns_constant(f):
    pass

def halts(f):
    def inner():
        f()
        return 0
    return returns_constant(inner)


# REFACTORING
# are two functions equivalent or not?
# is the refactored system the same as the original system 

def fns_are_equiv(f, g):
    pass

def halts(f):
    def inner():
        f()
        return 0
    def inner2():
        return 0
    return fns_are_equiv(inner, inner2)


# Idris programming language has a feature called a totality checker: whether your functions terminate or not, at compile time
# rejects the program if it's not total
total def():
    pass

# how?
# sometimes detects when it halts and when it doesn't.
# when it can't tell, it says that it doesn't halt
def conservative_halts(f):
    pass
