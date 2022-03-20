# Compiler from Scratch
Implementing the compiler from scratch in python instead of ruby.
https://www.destroyallsoftware.com/screencasts/catalog/a-compiler-from-scratch

## goals
- build a compiler from scratch, very simple
- define a function `f` with no arguments that returns a constant `1`
- we'll have a lexer, aka a tokenizer, and a code generator
  - three phases that almost every compiler has
  - there are other that we won't deal with but these three we need to get up and running

note that none of this code is efficient. we're just trying to do the simplest way possible.

## Tokenizer
need to break the codes into the smallest pieces possible. each element in the code, like (, ), end


## Parser
goal is to transform the token stream  (an array of our token objects created by the tokenizer) into a tree structure representing the structure of the code that was inputted into the compiler. needs to match the human's understanding of how the different pieces, the different tokens, are related

DEF
  NAME: "f"
  ARGS: ["x", "y", "z"]
  BODY:  # some kind of expression, function calls, etc   INTEGER_LITERAL: "1"

so our parser needs to create some sort of structure like this ^. that's what parsing is

## generator
recursively generates the call, sort of like how the parser recursively creates the output

```bash
python3 compiler-from-scratch/compiler.py | node
```

```bash
ruby compiler-from-scratch/compiler.py
```

## q's
consume/popping off the string/just going one by one and throwing the code and tokens away and updating the value of self.tokens or self.code...is this mutability common in OOP or compilers?
