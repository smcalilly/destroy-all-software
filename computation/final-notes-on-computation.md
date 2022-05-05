what is the grammar for a regex?
it's context-free because they require balanced parens

REGEX = REGEX '*'
REGEX = REGEX '|' REGEX
REGEX = '(' REGEX ')'
REGEX = REGEX REGEX


REGEX = 'a'
REGEX = 'b'
...etc

how to create a grammar? 
GRAMMER = DEF
GRAMMER = DEF GRAMMAR
DEF = SYMBOL '=' RHS '\n'
RHS = SYMBOL
RHS = LITERAL
RHS = SYMBOL RHS
RHS = LITERAL RHS
SYMBOL = CHAR
SYMBOL = CHAR SYMBOL
LITERAL = "''" CHAR "''"
CHAR = 'a'
CHAR = 'b'
...

a grammar for grammars. or a grammar for itself. is it regular or context-free? it's regular


---

turing machine and lambda calculus (1930s)

imperative programming vs functional programming


turing machine
  - large memory (tape) + CPU
modern computer:
  - large memory + CPU (fast) + memory bus (slow)


