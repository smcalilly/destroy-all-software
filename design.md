law of demeter
it's okay to access things that you made, or have passed into you. and it's okay to access attributes on those things, but it's not okay to access attributes on attributes on the thing.


a
a.b
a.b.c

a.b.c breaks the law of demeter
if user.cards.all?(&:invalid?)

tell don't ask
you should not inspect an object and based on it's state make a decision about what happens to it.

tell don't ask vs single responsibility

build small pieces that do cohesive things


tell don't ask
pulling information out of the object and then doing something to the object.
- ask with mutation
- ask without mutation
- tell with mutation
- tell without mutation