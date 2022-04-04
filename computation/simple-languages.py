# chomsky hierarchy
# regexs, regular grammars, finite state machines
# ...
# ...
# turing-equivalent (CPUs, TM, LC)



import re

RE = r"""
    (
        [123]
        [+*]
    )*
    [123]
"""

def recognize(s):
    return bool(re.match("^" + RE + "$", s, re.VERBOSE))


print(recognize('1'))
print(recognize('1+1'))
print(recognize('1*1'))
print(recognize('1*1+1'))
print(recognize('3*2+1'))
print('--')
print(recognize('3*2+z'))
print(recognize('3*2+'))



# we're gonna transform our regex into a simple grammar

r"""
    EXPR = NUM
    EXPR = NUM OP EXPR
    # EXPR = (NUM OP)* NUM
    NUM = '1'
    NUM = '2'
    NUM = '3'
    OP = '+'
    OP ='*'
"""

# right regular grammar
# RULE1 = '1'
# RULE1 = '1' RULE2
r"""
    EXPR = '1'
    EXPR = '2'
    EXPR = '3'
    EXPR = '1' OP_EXPR
    EXPR = '2' OP_EXPR
    EXPR = '3' OP_EXPR
    OP_EXPR = '+' EXPR
    OP_EXPR = "*" EXPR
"""

# how might we use this knowlege to implement a regex?
# 8:48

'3*2+1'

# we can do this with a finite state machine

# ken thompson (C, unix)
# thompson's construction (regex -> finite state machine)

