from .constants import digits

class Token:
    """Encapsulates the Token
    
    Arguments:
        type(:obj:`str`): the token of the lexeme
        value(:obj:`any`): the lexeme
        pos_start(:obj:`~Lex.position.Position`): the starting index of the lexeme
        pos_end(:obj:`~Lex.position.Position`): the end index of the lexeme

    Attributes:
        type(:obj:`str`): the token of the lexeme
        value(:obj:`any`): the lexeme

    """
    def __init__(self, type_, value=None, pos_start=None, pos_end=None):
        self.type = type_   
        self.value = value
        
        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()
        if pos_end:
            self.pos_end = pos_end
    
    def __repr__(self):
        """Representation for this :obj:`Token` object
        
        Returns:
            :obj:`str`: Object representation of :obj:`Token`
            
        """
        if self.value: return f'{self.type}: {self.value}'
        return f'{self.type}'

    def __str__(self):
        if self.value: return format(self.type,'>15') + '      ' + str(self.value)
        return f'{self.type}'


def print_tokens(tokens):
    """ Prints an array of :obj:`Token` in a table like format (type, value)

    Arguments:
        tokens(:obj:`list`): an array of :obj:`Token` 


    """
    for token in tokens:
        print(token.value)
    pass


def to_symbol_table(tokens):
    string = ''
    if(tokens != None):
        for token in tokens:
            string += str(token) + '\n'

    return string
