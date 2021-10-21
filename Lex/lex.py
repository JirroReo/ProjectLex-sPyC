from .tokens import Token
from .constants import digits, types
from .errors import IllegalCharacterError


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_character = None
        self.advance()
    
    def advance(self):
        self.pos += 1
        self.current_character = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_character is not None:
            if self.current_character in ' \t':
                self.advance()
            elif self.current_character in types:
                tokens.append(Token(types[self.current_character]))
                self.advance()
            elif self.current_character in digits:
                tokens.append(self.make_number())
            else:
                char = self.current_character
                self.advance()
                return [], IllegalCharacterError("'" + char +"'")

        return tokens, None
    
    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_character is not None and self.current_character in digits + '.':
            if self.current_character == '.':
                if dot_count > 0: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_character
            self.advance()

        if dot_count == 0:
            return Token('int', int(num_str))
        else:
            return Token('float', float(num_str))

def run(text):
    lexer = Lexer(text)
    tokens, errors = lexer.make_tokens()

    return tokens, errors

