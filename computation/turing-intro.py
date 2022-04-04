# X_B
# 
# BB
# ^

# X_B machine

# see B, turn into X
# B -> X
# X -> B

# head always have to move
# B -> X, R, 
# B -> B, L
# X -> B, R
# B -> B, L

# ordering
# lefthand side is a trigger

# state symbol: s1...s4
# used to sequence the 4 instructions



# s1: BB
#     ^
# s2: XB
#      ^

# ordering doesn't matter
# B, s2 -> B, L s3
# X, s3 -> B, R, s4
# B, s4 -> B, L, s1
# B, s1 -> X, R, s2

# B, s1 -> X, R, s2
# B, s2 -> B, L s3
# X, s3 -> B, R, s4
# B, s4 -> B, L, s1

X_B = {
 ('B', 's1'): ('X', 'R', 's2'),
 ('B', 's2'): ('B', 'L', 's3'),
 ('X', 's3'): ('B', 'R', 's4'),
 ('B', 's4'): ('B', 'L', 's1'),
}

def simulate(instructions):
    # setup initial state
    # tape, head, and state
    # tape = ['B', 'B'] # can be any size
    # head = 0
    # state = 's1' # this wouldn't be hardcoded in a true turing machine
    # 
    # # loop
    #     # look up an instruction
    #     # apply that instruction to the machine
    # 
    # # hardcoding loop, but it can be an infinite loop
    # for _ in range(8):
    #     print(state.rjust(4) + ': ' + ''.join(tape))
    #     print('      ' + ' ' * head + '^')
    #     tape[head], head_dir, state = instructions[(tape[head], state)]
    # 
    #     head += 1 if head_dir == 'R' else -1
    
    tape, head, state = ['B', 'B'], 0, 's1'

    for _ in range(8):
        tape[head], head_dir, state = instructions[(tape[head], state)]
        
        head += 1 if head_dir == 'R' else -1

simulate(X_B)

# head += 1 if head_dir == 'R' else -1
#  this could have a case where you don't move, making this statement have three conditions
# this is how you make computation instructions. it can be as complex as thousands of conditions
