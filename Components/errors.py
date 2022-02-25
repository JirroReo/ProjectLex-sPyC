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
        result = '\n' + f'{self.error_name}: {self.details}'
        result += f'\nFile {self.pos_start.fn}, line {self.pos_start.ln + 1}\n'
        result += '\n\n' + strWithArrows(self.pos_start.ftxt, self.pos_start, self.pos_end) 
        return result

class IllegalCharacterError(Error):
    """Error object for illegal character"""
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)

class InvalidSyntaxError(Error):
    """Error object for invalid syntax"""
    def __init__(self, pos_start, pos_end, details=''):
        super().__init__(pos_start, pos_end, 'Invalid Syntax', details)

class RTError(Error):
    """Error object for invalid syntax"""
    def __init__(self, pos_start, pos_end, details, context):
        super().__init__(pos_start, pos_end, 'Runtime Error', details)
        self.context = context

    def __str__(self):
        """The function that is invoked when passed in the :obj:`print` function"""
        result = self.generate_traceback()
        result += '\n' + f'{self.error_name}: {self.details}'
        result += '\n\n' + strWithArrows(self.pos_start.ftxt, self.pos_start, self.pos_end)
        return result

    def generate_traceback(self):
        result = ''
        pos = self.pos_start
        ctx = self.context

        while ctx:
            result += f'    File {pos.fn}, line {str(pos.ln + 1)}, in {ctx.display_name}\n' + result
            pos = ctx.parent_entry_pos
            ctx = ctx.parent

        return 'Traceback (most recent call last):\n' + result

class ExpectedCharError(Error):
    """Error object for expected character"""
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Expected Character: ', details)
class RTResult:
    def __init__(self):
        self.value = None
        self.error = None

    def register(self, res):
        if res.error: self.error = res.error
        return res.value
    
    def success(self, value):
        self.value = value
        return self

    def failure(self, error):
        self.error = error
        return self