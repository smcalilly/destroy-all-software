context-free grammar

function f() return 1

creates a parse tree:

stat
  'function'
  funcname
    dottedname
      NAME ('f')
  funcbody
    params
      '('
        parlist
        ''
      ')'
    block
      ...
    end

function f() ... end

example: create a minifier for javascript. you parse the code into a tree and change the tree in whatever way you like to minify it. you recurse down through the three to every single literal and dumps them out as your output.

compiler works a similar way. translate one tree into another kind of tree...one language tree
into a different lanugage tree. dumps that second tree out. first tree might be a C parse tree and the second might be an assembly tree, for a C compiler


how do these literals ('function', 'return', '(') work?
lexing (lexical analysis, tokenization): 
- turns code into a series of tokens.
- in most languages (like lua our example), lexing process is a regular process. it's very common to use regular expressions to take a string like our function and turn it into a series of tokens

however in python there's some weirdness
python has a "context-sensitive" lexer, the three level above context-free

lua: lex (regular) -> parse (context-free)
python: lex (context-sensitive) -> parse (context-free)
  - python's indentation requires the lexer to be context-sensitive. also true of haskell bc it's whitespace depdent


