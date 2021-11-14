from Components.tokens import Token
from Components.constants import TYPE_EOF, digits, alphabet, keywords, reserved_words, special_characters, delimiters, types
from Components.errors import IllegalCharacterError, UnexpectedCharacterError
from Components.position import Position

class Lexer:
    """ Lexical Analyzer class

        This class encapsulates all the operations of the lexical analyzer

        Args:
            fn (:obj:`str`): The file name
            text (:obj:`str`): The string of characters stored in :obj:`fn` file

        Attributes:
            fn (:obj:`str`): Filename where the :attr:`text` is stored
            text (:obj:`str`): String of text to be analyzed by the Lexer
            pos (:obj:`~Lex.position.Position`): The Position object that encapsulates the text, movement, and location of the scanner
            current_character(:obj:`str`): Current character from the text

    """

    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_character = None
        self.advance()
        self.tokens = []
    
    def advance(self):
        """Calls the :meth:`~Lex.position.Position.advance` method of :attr:`pos` to get the next character in the :attr:`text` """

        self.pos.advance(self.current_character)
        self.current_character = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def make_tokens(self):
        """ Analyzes lexemes in :attr:`text` and converts it to :class:`~Lex.tokens.Token` and stores the results in a :obj:`list`
        
        Returns:
            tuple: If success: tokens(:obj:`str`), None; otherwise, [], :class:`~Lex.errors.IllegalCharacterError`

        """

        # tokens = [] # store the list of tokens  ---> i made this variable an instance variable

        while self.current_character is not None:# loop while there is a character to read
            if self.current_character in delimiters:# if the character is a tab or space, ignore
                self.advance()

            elif self.current_character in special_characters:# if the current character is in types, push the token
                if(self.current_character == '\'' or self.current_character == '"'):
                    end_signal = self.current_character # save the character used to start the string literal (either ' or ")
                    str_literal = self.current_character
                    self.advance()

                    while(self.current_character != end_signal):
                        str_literal += self.current_character
                        self.advance()

                    str_literal += self.current_character #add the string literal terminator to the string (either ' or ")
                    self.tokens.append(Token("STR_LIT", str_literal, pos_start=self.pos))
                    self.advance()

                else: 
                    self.tokens.append(Token(special_characters[self.current_character], self.current_character, pos_start=self.pos))
                    self.advance()

            elif self.current_character in digits:# if the current character is in the digits, create number
                self.tokens.append(self.make_number())
                
            elif self.current_character in alphabet:# if the current character is in the alphabet, check if identifier or keywords
                output = self.make_lexeme()
                if(isinstance(output, Token)):
                    self.tokens.append(output)
                else:
                    return output

            else:# If the character didn't pass all the other conditions, return an error
                pos_start = self.pos.copy()
                char = self.current_character
                self.advance()
                return [], IllegalCharacterError(pos_start, self.pos, "'" + char +"'")

        self.tokens.append(Token("TYPE_EOF", TYPE_EOF, pos_start=self.pos)) #Append the EOF token
        return self.tokens, None
    
    def make_number(self):
        """Create a number token
        
        Returns:
            :class:`~Lex.tokens.Token`: A :class:`~Lex.tokens.Token` which is either has a :attr:`~Lex.tokens.Token.type` attribute 
            containing either :obj:`int` or :obj:`float` (only these two are supported as of now) 

        """
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
            return Token('INT_LIT', int(num_str), pos_start, self.pos)
        else:
            return Token('FLOAT_LIT', float(num_str), pos_start, self.pos)

    def make_lexeme(self):
        """Captures :obj:`identifier`, :obj:`~Lex.constants.keywords`, and :obj:`~Lex.constants.reserved_words` lexemes 
        
        Returns:
            :class:`~Lex.tokens.Token`: A :class:`~Lex.tokens.Token` which has an attribute :attr:`~Lex.tokens.Token.type` having a value of either "identifier", "keywords", or "reserved words" 

        """

        lexeme = ''
        pos_start = self.pos.copy()

        # assuming (for now) that identifiers can only contain alphabet and digits
        while self.current_character is not None and (self.current_character in alphabet or self.current_character in digits):
            if(len(self.tokens) > 0 and not(self.tokens[-1].value == 'def' or self.tokens[-1].value == 'class')):
                if(self.current_character.isupper()):
                    if(not(lexeme in types)):
                        return [], UnexpectedCharacterError(pos_start, self.pos, "'" + self.current_character +"'")
            lexeme += self.current_character
            self.advance()
            

        #checks if the lexeme matches a keyword or reserved word, otherwise consider as identifier
        if(lexeme in keywords):
            return Token('KEYWORD', lexeme, pos_start, self.pos)
        elif(lexeme in reserved_words):
            return Token('RESERVED_WORD', lexeme, pos_start, self.pos)
        elif(lexeme in types):
            return Token("DATA_TYPE", types[lexeme], pos_start, self.pos)
        else:
            return Token('IDENTIFIER', lexeme, pos_start, self.pos)
