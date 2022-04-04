# # gonna convert this into lambda calculus with all the constructs available
# # can't use def, if, equal signs, returns
# # we can only use definitions of functions with exactly one argument and calls to functions with exactly one argument
# # def fact(n):
# #     if n == 0:
# #         return 1
# #     else:
# #         return n * fact(n - 1)
# 
# 
# 
# 
# ONE = 1
# IS_ZERO = lambda x: x == 0
# SUB1 = lambda x: x - 1
# MULT = lambda x: lambda y: x * y
# IF = lambda cond: lambda t_func: lambda f_func: t_func(None) if cond else f_func(None)
# 
# 
# 
# print(
#     (
#         lambda myself: (
#             lambda n: (
#                 IF(
#                     IS_ZERO(n)
#                 )(
#                     lambda _: ONE
#                 ) (
#                     lambda _: MULT(n)( myself(myself)(SUB1(n)) )
#                 )
#             )
#         )
#     )(
#         lambda myself: (
#             lambda n: (
#                 IF(
#                     IS_ZERO(n)
#                 )(
#                     lambda _: ONE
#                 ) (
#                     lambda _: MULT(n)( myself(myself)(SUB1(n)) )
#                 )
#             )
#         )
#     )
#     (6)
# )

# church numeral from alozonzo church
ZERO = lambda f: lambda x: x
ONE = lambda f: lambda x: f(x) # apply f one time
TWO = lambda f: lambda x: f(f(x)) # apply f two times
THREE = lambda f: lambda x: f(f(f(x)))

# give the argument n as TWO and it returns a new church numeral that delegates to an existing church numeral
# IDENTITY = lambda n: (lambda f: lambda x: n(f)(x))

ADD1 = lambda n: (lambda f: lambda x: f( n(f)(x) ))

ADD = lambda n: lambda m: n(ADD1)(m)

MULT = lambda n: lambda m: n(lambda acc: ADD(m)(acc))(ZERO)

print(
    MULT(
        TWO
    )(
        MULT(
            THREE
        )(
            THREE
        )
    )
    (lambda x: x + 1)(0)
)

# print(
#     MULT(
#         TWO
#     )(
#         THREE
#     )
#     (lambda x: x + 1)(0)
# )

# print(
#     ADD(
#         TWO
#     )(
#         THREE
#     )
#     (lambda x: x + 1)(0)
# )


# print(
#     ADD1(
#         ADD1(
#             TWO
#         )
#     )
#     (lambda x: x + 1)(0)
# )
