from pathlib import Path
from collections import OrderedDict
import re
from dataclasses import dataclass
from typing import List

@dataclass
class Token:
    type: str
    value: str

@dataclass
class DefNode:
    name: str
    arg_names: list
    body: object

@dataclass
class IntegerNode:
    value: int

@dataclass
class VarRefNode:
    value: str

@dataclass
class CallNode:
    name: str
    arg_exprs: list # todo, can you do a list of different types? like in type hints

class Tokenizer:
    TOKEN_TYPES = [
        ('def', r'\bdef\b'),
        ('end', r'\bend\b'),
        ('identifier', r'\b[a-zA-Z]+\b'),
        ('integer', r'\b[0-9]+\b'),
        ('oparen', r'\('),
        ('cparen', r'\)'),
        ('comma', r',')
    ]

    def __init__(self, code):
        self.code = code

    def tokenize(self) -> List[Token]:
        tokens = []

        while self.code:
            token = self.tokenize_one_token()
            tokens.append(token)

        return tokens

    def tokenize_one_token(self) -> Token:
        for type, regex in self.TOKEN_TYPES:

            if match := re.match(regex, self.code):
                value = match.group()
                self.code = self.code[len(value):].strip()
                return Token(type=type, value=value)

        raise RuntimeError(f'Could not match token on code: "{self.code}"')

# TODO: would be nice to have the tokens as their own types instead of just passing strings?
# or maybe enum?


class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens

    def parse(self):
        return self.parse_def()

    def parse_def(self) -> DefNode:
        self.consume('def')
        name = self.consume('identifier').value
        arg_names = self.parse_arg_names()
        body = self.parse_expr()

        return DefNode(
            name=name,
            arg_names=arg_names,
            body=body
        )

    def consume(self, expected_type: str) -> Token:
        token = self.tokens.pop(0)

        if token.type == expected_type:
            return token
        else:
            raise RuntimeError(
                f'Expected token type {expected_type} but got {token.type}'
            )

    def peek(self, expected_type, offset=None) -> bool:
        if not offset:
            offset = 0

        return self.tokens[offset].type == expected_type

    def parse_arg_names(self) -> List:
        arg_names = []

        self.consume('oparen')

        if self.peek('identifier'):
            arg_names.append(self.consume('identifier').value)

            while self.peek('comma'):
                self.consume('comma')
                arg_names.append(self.consume('identifier').value)

        self.consume('cparen')

        return arg_names

    def parse_expr(self):
        if self.peek('integer'):
            return self.parse_integer()
        elif self.peek('identifier') and self.peek('oparen', offset=1):
            return self.parse_call()
        else:
            return self.parse_var_ref()

    def parse_integer(self) -> IntegerNode:
        return IntegerNode(
            value=int(self.consume('integer').value)
        )

    def parse_call(self) -> CallNode:
        name = self.consume('identifier')
        arg_exprs = self.parse_arg_exprs()
        return CallNode(name.value, arg_exprs)

    def parse_arg_exprs(self) -> List:
        arg_exprs = []

        self.consume('oparen')

        if not self.peek('cparen'):
            expression = self.parse_expr()
            arg_exprs.append(expression)

            while self.peek('comma'):
                self.consume('comma')

                expression = self.parse_expr()
                arg_exprs.append(expression)

        self.consume('cparen')

        return arg_exprs

    def parse_var_ref(self) -> VarRefNode:
        return VarRefNode(
            value=self.consume('identifier').value
        )

class Generator:
    def generate(self, node):
        if type(node) == DefNode:
            return 'function {name}({args}) {{ return {body} }};'.format(
                name=node.name,
                args=', '.join(node.arg_names),
                body=self.generate(node.body)
            )

        elif type(node) == CallNode:
            return '{name}({args})'.format(
                name=node.name,
                args=', '.join(map(self.generate, node.arg_exprs))
            )

        elif type(node) == VarRefNode:
            return node.value

        elif type(node) == IntegerNode:
            return node.value
        else:
            raise RuntimeError(f'Unexpected node type: {node}')


file_path = Path(__file__).with_name('test.src')
with file_path.open('r') as f:
    tokenizer = Tokenizer(code=f.read().rstrip())

tokens = tokenizer.tokenize()

tree = Parser(tokens=tokens).parse()

RUNTIME = "function add(x, y) { return x + y };"
TEST = "console.log(f(1, 2));"
generated = Generator().generate(tree)
print('\n'.join([RUNTIME, generated, TEST]))
