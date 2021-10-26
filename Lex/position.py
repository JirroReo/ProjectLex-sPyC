class Position:
    """Class that encapsulates the positioning of the lexical analyzer to the given string of characters
    
    Attributes:

        idx(:obj:`int`): the index in the ftxt
        ln(:obj:`int`): the line number
        col(:obj:`int`): the column number
        fn(:obj:`string`): filename
        ftxt(:obj:`string`): the string of characters from the file named :attr:`fn`

    """
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt
    
    def advance(self, current_character=None):
        """Increment the index (:attr:`idx`) by 1
        
        Increments the :attr:`ln` and resets the :attr:`col` to 0 if it encounters the new line character

        Params:
            current_character(:obj:char): The current character in the :attr:`ftxt` in the index :attr:`idx` (Position.ftxt[idx]);
        """
        self.idx += 1
        self.col += 1

        if current_character == '\n':
            self.ln += 1
            self.col = 0
        
        return self
    
    def copy(self):
        """Creates a new :obj:`Position` object identical to the calling instance"""
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)
