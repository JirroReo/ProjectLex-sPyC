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
    
    def matches(self, type_, value):
        return self.type == type_ and self.value == value
    
    def __repr__(self):
        """Representation for this :obj:`Token` object
        
        Returns:
            :obj:`str`: Object representation of :obj:`Token`
            
        """
        if self.value: return f'{self.type}: {self.value}'
        return f'{self.type}'