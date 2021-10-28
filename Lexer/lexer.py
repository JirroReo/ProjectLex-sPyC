from Components.tokens import Token
from Components.constants import TYPE_EOF, digits, types, alphabet, keywords, reserved_words
from Components.errors import IllegalCharacterError
from Components.position import Position

class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_character = None
        self.advance()
    
    def advance(self):
        self.pos.advance(self.current_character)
        self.current_character = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_character is not None:
            if self.current_character in ' \t':
                self.advance()
            elif self.current_character in types:
                tokens.append(Token(types[self.current_character], pos_start=self.pos))
                self.advance()
            elif self.current_character in digits:
                tokens.append(self.make_number())
            elif self.current_character in alphabet:
                tokens.append(self.make_lexeme())
            else:
                pos_start = self.pos.copy()
                char = self.current_character
                self.advance()
                return [], IllegalCharacterError(pos_start, self.pos, "'" + char +"'")

        tokens.append(Token(TYPE_EOF, pos_start=self.pos)) #End of file identifier
        return tokens, None
    
    def make_number(self):
        num_str = ''
        dot_count = 0
        pos_start = self.pos.copy()

        while self.current_character is not None and self.current_character in digits + '.':
            if self.current_character == '.':
                if dot_count > 0: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_character
            self.advance()

        if dot_count == 0:
            return Token('INT', int(num_str), pos_start, self.pos)
        else:
            return Token('FLOAT', float(num_str), pos_start, self.pos)

    def make_lexeme(self):
        lexeme = ''
        pos_start = self.pos.copy()

        # assuming (for now) that identifiers can only contain alphabet and digits
        while self.current_character is not None and (self.current_character in alphabet or self.current_character in digits):
            lexeme += self.current_character
            self.advance()
            

        #checks if the lexeme matches a keyword or reserved word, otherwise consider as identifier
        if(lexeme in keywords):
            return Token('KEYWORD', lexeme, pos_start, self.pos)
        elif(lexeme in reserved_words):
            return Token('RESERVED_WORD', lexeme, pos_start, self.pos)
        else:
            return Token('IDENTIFIER', lexeme, pos_start, self.pos)
