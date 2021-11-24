from Utils.string_with_arrows import string_with_arrows as strWithArrows

class Error:
    """The base error class
    
    Attributes:
        pos_start(int): the starting position of the error in the text
        pos_end(int): the end position of the error in the text
        error_name(str): name of the error
        details(str): details of the error

    """
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
    
    def __str__(self):
        """The function that is invoked when passed in the :obj:`print` function"""
        result = '\n\n' + strWithArrows(self.pos_start.ftxt, self.pos_start, self.pos_end) 
        result += '\n' + f'{self.error_name}: {self.details}'
        result += f'\nFile {self.pos_start.fn}, line {self.pos_start.ln + 1}\n'
        return result

class IllegalCharacterError(Error):
    """Error object for illegal character"""
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)

class InvalidSyntaxError(Error):
    """Error object for invalid syntax"""
    def __init__(self, pos_start, pos_end, details=''):
        super().__init__(pos_start, pos_end, 'Invalid Syntax', details)

class UnexpectedCharacterError(Error):
    """Error object for illegal character"""
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Unexpected Character', details)