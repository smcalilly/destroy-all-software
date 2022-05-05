regular:
a*b*

context-free:
a{n}b{n}

context-senstive:
a{n}b{n}c{n}

S     = ''
S     = 'a' S B C
C B   = B C
'a' B = 'a' 'b'
'b' B = 'b' 'b'
'b' C = 'b' 'c'
'c' C = 'c' 'c'

replacing multiple things instead of  a single thing

he takes this string and converts it with the language
"aabbcc"

parsing perl is undecidable, like the halting problem
