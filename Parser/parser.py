from Components.nodes import NumberNode, BinOpNode, UnaryOpNode, VarAccessNode, VarAssignNode
from Components.errors import InvalidSyntaxError
from Components.constants import TYPE_EOF

class ParseResult:
    def __init__(self):
        self.error = None
        self.node = None
        self.advance_count = 0

    def register_advancement(self):
        self.advance_count += 1

    def register(self, res):
        self.advance_count += res.advance_count
        if res.error: self.error = res.error
        return res.node

    def success(self, node):
        self.node = node
        return self
    
    def failure(self, error):
        if not self.error or self.advance_count == 0:
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
        if not res.error and self.current_tok.type is not TYPE_EOF:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                "Expected '+', '-', '*', '/', or '%'"
            ))
        return res

    def atom(self):
        res = ParseResult()
        tok = self.current_tok

        if tok.type in ('INT_LIT', 'FLOAT_LIT'):
            res.register_advancement()
            self.advance()
            return res.success(NumberNode(tok))
        
        elif tok.type == 'IDENTIFIER':
            res.register_advancement()
            self.advance()
            return res.success(VarAccessNode(tok))
        
        elif tok.type == 'LPAREN':
            res.register_advancement()
            self.advance()
            expression = res.register(self.expression())
            if res.error: return res
            if self.current_tok.type == 'RPAREN':
                res.register_advancement()
                self.advance()
                return res.success(expression)
            else: 
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected ')'"
                ))

        return res.failure(InvalidSyntaxError(
            tok.pos_start, tok.pos_end,
            "Expected int, float, identifier, '+', '-', or '('"
        ))
                

    def power(self):
        return self.bin_op(self.atom, ('RAISED TO', ), self.factor) # Dont remove comma, we need to pass a tuple
        
    def factor(self):
        res = ParseResult()
        tok = self.current_tok

        if tok.type in ('PLUS', 'MINUS'):
            res.register_advancement()
            self.advance()
            factor = res.register(self.factor())
            if res.error: return res
            return res.success(UnaryOpNode(tok, factor))

        return self.power()

    def term(self):
        return self.bin_op(self.factor, ('MODULO', 'MULTIPLY', 'DIVIDE'))

    def expression(self):
        res = ParseResult()

        if self.current_tok.matches('KEYWORD', 'var'):
            res.register_advancement()
            self.advance()
            if self.current_tok.type != 'IDENTIFIER':
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    'Expected identifier'
                ))
            
            var_name = self.current_tok
            res.register_advancement()
            self.advance()

            if self.current_tok.type != 'EQUALS':
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    'Expected \'=\''
                ))

            res.register_advancement()
            self.advance()
            expr = res.register(self.expression())
            if res.error: 
                return res
            return res.success(VarAssignNode(var_name, expr))

        node = res.register(self.bin_op(self.term, ('PLUS', 'MINUS')))

        if res.error: return res.failure(InvalidSyntaxError(
            self.current_tok.pos_start, self.current_tok.pos_end,
            "Expected int, float, identifier, 'var', '+', '-', or '('"
        ))
        return res.success(node)

    def bin_op(self, func_a, ops, func_b=None):
        if func_b is None:
            func_b = func_a

        res = ParseResult()
        left = res.register(func_a())
        if res.error: return res

        while self.current_tok.type in ops:
            op_tok = self.current_tok
            res.register_advancement()
            self.advance()
            right = res.register(func_b())
            if res.error: return res
            left = BinOpNode(left, op_tok, right)
        
        return res.success(left)
