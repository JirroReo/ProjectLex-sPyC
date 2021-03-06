from Components.tokens import Token
from Components.constants import TYPE_EOF, digits, alphabet, keywords, reserved_words, special_characters, delimiters, types, operators, spaces, constants, boolean_literal
from Components.errors import IllegalCharacterError, UnexpectedCharacterError, InvalidSyntaxError
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

        while self.current_character is not None: # loop while there is a character to read

            if self.current_character in spaces: # ignore spaces
                self.advance()

            elif self.current_character in delimiters: # if the character is a tab or space, ignore
                output = self.scan_delimeter()
                if(isinstance(output, Token)):
                    self.tokens.append(output)

            elif self.current_character in special_characters: # if the current character is in types, push the token
                if self.current_character == '#': # check if the current character is a comment indicator
                    output = self.scan_comment()
                    if(isinstance(output, Token)):
                        self.tokens.append(output)
                    else:
                        return [], output

                elif(self.current_character == '\'' or self.current_character == '"'): # check whether the current character is a string indicator
                    output = self.scan_string_literal()
                    if(isinstance(output, Token)):
                        self.tokens.append(output)
                    else:
                        return [], output
            
                else: # create a token for the special character
                    output = self.scan_special_character()
                    if(isinstance(output, Token)):
                        self.tokens.append(output)
                    else:
                        return [], output

            elif self.current_character in operators:
                output = self.scan_operator()
                if(isinstance(output, Token)):
                    self.tokens.append(output)
                else:
                    return [], output

            elif self.current_character in digits: # if the current character is in the digits, create number
                output = self.make_number()
                if(isinstance(output, Token)):
                    self.tokens.append(output)
                else:
                    return [], output

            elif self.current_character in alphabet: # if the current character is in the alphabet, check if identifier or keywords
                output = self.make_lexeme()
                if(isinstance(output, Token)):
                    self.tokens.append(output)
                else:
                    return [], output

            else:# If the character didn't pass all the other conditions, return an error
                pos_start = self.pos.copy()
                char = self.current_character
                self.advance()
                return [], IllegalCharacterError(pos_start, self.pos, "'" + char +"'")

        self.tokens.append(Token("TYPE_EOF", TYPE_EOF, pos_start=self.pos)) #Append the EOF token
        return self.tokens, None
    
    def scan_delimeter(self):
        token = Token(delimiters[self.current_character], self.current_character, self.pos, self.pos)
        self.advance()

        return token
        
    def scan_comment(self):
        pos_start = self.pos.copy()
        lexeme = self.current_character
        self.advance()
        while(self.current_character != '#'): # get all the characters until # is not encountered
            if(self.current_character == '\n' or self.current_character is None): # check if comment is unterminated
                return InvalidSyntaxError(pos_start, self.pos, 'Comments must be terminated with another \'#\'.')
            else: 
                lexeme += self.current_character
                self.advance()

        lexeme += self.current_character
        self.advance()
        
        return Token("COMMENT", lexeme, pos_start, self.pos)
        
    def scan_string_literal(self):
        end_signal = self.current_character # save the character used to start the string literal (either ' or ")
        str_literal = self.current_character
        self.advance()

        while(self.current_character != end_signal):
            str_literal += self.current_character
            self.advance()

        str_literal += self.current_character #add the string literal terminator to the string (either ' or ")
        self.advance()
        return Token("STR_LIT", str_literal, pos_start=self.pos)

    def scan_special_character(self):
        token = Token(special_characters[self.current_character], self.current_character, pos_start=self.pos)
        self.advance()

        return token
        
    def scan_operator(self):
        """Scan operator lexemes"""
        pos_start = self.pos.copy()
        operator = self.current_character
        self.advance()

        while(self.current_character in operators):
            operator += self.current_character
            self.advance()
            if operator not in operators:
                illegal_pos = self.pos.copy()
                illegal_pos.idx -= 1
                return UnexpectedCharacterError(pos_start, illegal_pos, "'" + self.text[illegal_pos.idx] + "'")
        
        return Token(operators[operator], operator, pos_start, self.pos)
            

    def make_number(self):
        """Create a number token
        
        Returns:
            :class:`~Lex.tokens.Token`: A :class:`~Lex.tokens.Token` which is either has a :attr:`~Lex.tokens.Token.type` attribute 
            containing either :obj:`int` or :obj:`float` (only these two are supported as of now) 

        """
        num_str = ''
        dot_count = 0
        pos_start = self.pos.copy()
        is_illegal = False

        while self.current_character is not None and self.current_character in digits + alphabet + '.':
            if self.current_character == '.':
                if dot_count > 0: break
                dot_count += 1
                num_str += '.'
            elif self.current_character in alphabet:
                is_illegal = True
            else:
                num_str += self.current_character
            self.advance()

        if is_illegal: 
                return InvalidSyntaxError(pos_start, self.pos, "Identifiers can't start with a digit.")
        elif dot_count == 0:
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
        isDoneCheckingIdentifierFormat = False
        if(self.current_character.isupper()):
            while self.current_character is not None and (self.current_character in alphabet or self.current_character in digits):
                lexeme += self.current_character
                self.advance()
        else:
            while self.current_character is not None and (self.current_character in alphabet or self.current_character in digits):
                if(not(isDoneCheckingIdentifierFormat) and (len(self.tokens) > 0)):
                    index = -1
                    while((index + len(self.tokens) != 0) and self.tokens[index].value in delimiters):
                        index -= 1
                    if(not(self.tokens[index].value == 'def' or self.tokens[index].value == 'class')):
                        if(self.current_character.isupper()):
                            if(not(lexeme in types)):
                                return UnexpectedCharacterError(pos_start, self.pos, "'" + self.current_character +"'")
                            isDoneCheckingIdentifierFormat = True
                lexeme += self.current_character
                self.advance()
            
        if(lexeme == 'quit'): # if lexeme is quit then stop program.
            exit()
    
        # checks if the lexeme matches a keyword or reserved word, otherwise consider as identifier
        if(lexeme in keywords):
            return Token('KEYWORD', lexeme, pos_start, self.pos)
        elif(lexeme in reserved_words):
            return Token('RESERVED_WORD', lexeme, pos_start, self.pos)
        elif(lexeme in types):
            return Token("DATA_TYPE", types[lexeme], pos_start, self.pos)
        elif(lexeme in constants):
            return Token("CONSTANT", lexeme, pos_start, self.pos)
        elif(lexeme in boolean_literal):
            return Token("BOOLEAN_LITERAL", lexeme, pos_start, self.pos)    
        else:
            return Token('IDENTIFIER', lexeme, pos_start, self.pos)
