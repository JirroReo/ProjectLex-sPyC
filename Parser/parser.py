from Components.nodes import NumberNode, BinOpNode, UnaryOpNode
from Components.errors import InvalidSyntaxError
from Components.constants import TYPE_EOF

class ParseResult:
    def __init__(self):
        self.error = None
        self.node = None

    def register(self, res):
        if isinstance(res, ParseResult):
            if res.error: self.error = res.error
            return res.node
        
        return res

    def success(self, node):
        self.node = node
        return self
    
    def failure(self, error):
        self.error = error
        return self

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = -1       #Token index
        self.advance()
    
    def advance(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok
    
    def parse(self):
        res = self.expression()
        if res.error and self.current_tok.type is not TYPE_EOF:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                "Expected '+', '-', '*', '/', or '%'"
            ))
        return res

    def atom(self):
        res = ParseResult()
        tok = self.current_tok

        if tok.type in ('PLUS', 'MINUS'):
            res.register(self.advance())
            factor = res.register(self.factor())
            if res.error: return res
            return res.success(UnaryOpNode(tok, factor))

        elif tok.type in ('INT_LIT', 'FLOAT_LIT'):
            res.register(self.advance())
            return res.success(NumberNode(tok))
        
        elif tok.type == 'LPAREN':
            res.register(self.advance())
            expression = res.register(self.expression())
            if res.error: return res
            if self.current_tok.type == 'RPAREN':
                res.register(self.advance())
                return res.success(expression)
            else: 
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected ')'"
                ))

        return res.failure(InvalidSyntaxError(
            tok.pos_start, tok.pos_end,
            "Expected '+', '-', 'int', 'float', or '('"
        ))
                

    def power(self):
        return self.bin_op(self.atom, ('RAISED TO', ), self.factor) # Dont remove comma, we need to pass a tuple
        
    def factor(self):
        res = ParseResult()
        tok = self.current_tok

        if tok.type in ('PLUS', 'MINUS'):
            res.register(self.advance())
            factor = res.register(self.factor())
            if res.error: return res
            return res.success(UnaryOpNode(tok, factor))

        return self.power()

    def term(self):
        return self.bin_op(self.factor, ('MODULO', 'MULTIPLY', 'DIVIDE'))

    def expression(self):
        return self.bin_op(self.term, ('PLUS', 'MINUS'))

    def bin_op(self, func_a, ops, func_b=None):
        if func_b is None:
            func_b = func_a

        res = ParseResult()
        left = res.register(func_a())
        if res.error: return res

        while self.current_tok.type in ops:
            op_tok = self.current_tok
            res.register(self.advance())
            right = res.register(func_b())
            if res.error: return res
            left = BinOpNode(left, op_tok, right)
        
        return res.success(left)
