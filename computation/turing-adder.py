ADDER = {
    # (11+111)BBBBBBB ->
    #    ^
    ('B', 's1'): ('(', 'R', 's2'),
    ('B', 's2'): ('1', 'R', 's3'),
    ('B', 's3'): ('1', 'R', 's4'),
    ('B', 's4'): ('+', 'R', 's5'),
    ('B', 's5'): ('1', 'R', 's6'),
    ('B', 's6'): ('1', 'R', 's7'),
    ('B', 's7'): ('1', 'R', 's7b'),
    ('B', 's7b'): ('1', 'R', 's8'),
    ('B', 's8'): (')', 'R', 's9'),
    
    ('B', 's9'): ('B', 'L', 's9'),
    (')', 's9'): (')', 'L', 's9'),
    ('1', 's9'): ('1', 'L', 's9'),
    ('+', 's9'): ('1', 'R', 's10'),
    
    ('1', 's10'): ('1', 'R', 's10'),
    (')', 's10'): ('B', 'L', 's11'),
    
    ('1', 's11'): (')', 'R', 's12'),
    ('B', 's12'): ('B', 'R', 's12'),
}

def simulate(instructions):
    tape = ['B'] * 16
    head = 0
    state = 's1'
    
    for _ in range(24):
        print(state.rjust(4) + ': ' + ''.join(tape))
        print('      ' + ' ' * head + '^')

        tape[head], head_dir, state = instructions[(tape[head], state)]
        head += 1 if head_dir == 'R' else -1

simulate(ADDER)

# gonna show how this is as powerful as a laptop.
# gonna show three different properties of computational systems
# that when combined look a lot like general purpose computing
# 1. repetition
# 2. conditionals
# 3. data structures that contain other data structures

# 1. our xb machine already has repetition bc it continues to repeat the same thing

# 2. already has a kind of conditional. if we delete the third instruction, the three
# remaining instructions 1, 2, 4 all trigger on the B but different state symbols.
# we can think of that as a conditional: does different things on different states

# not allowed to have a infinite set of symbols.
# a turning machine must have a finite set of tape symbols that are specified in advance
# of the machine running.
# we can have binary like real computers, complex to implement but would work
# so we're gonna go simpler and use unary numbers:
# 1, 11, 11, 1111
# addtion: (11 + 111) = 11111
# how to do that with BBBBB
# (11+111)BBBBBBB ->
#    ^
# (111111)BBBBBBB
#        ^
# (111111BBBBBBBB
#       ^
# (11111)BBBBBBBB

# list:
# (1,11,111)
# string:
# 'DAD' = (1111,1,1111)
# list of lists: (aka a tree)
# ((1,11),(111,1111))

# anything expressable on my laptop is expressable in a turing machine, and
# any turing machine is runnable on my laptop
