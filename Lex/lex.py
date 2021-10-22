from .tokens import Token
from .constants import digits, types, alphabet, keywords, reserved_words
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
            elif self.current_character in alphabet:
                tokens.append(self.make_lexeme())
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

    def make_lexeme(self):
        lexeme = ''
        # assuming (for now) that identifiers can only contain alphabet and digits
        while self.current_character is not None and (self.current_character in alphabet or self.current_character in digits):
            lexeme += self.current_character
            self.advance()
            

        #checks if the lexeme matches a keyword or reserved word, otherwise consider as identifier
        if(lexeme in keywords):
            return Token('Keyword', lexeme)
        elif(lexeme in reserved_words):
            return Token('Reserved_word', lexeme)
        else:
            return Token('Identifier', lexeme)

def run(text):
    lexer = Lexer(text)
    tokens, errors = lexer.make_tokens()

    return tokens, errors
