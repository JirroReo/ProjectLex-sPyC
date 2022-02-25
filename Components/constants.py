TYPE_EOF = 'End of file'
"""str: The end of file constant"""
ASSIGN = '='
EQ = '=='
NEQ = '!='
GT = '>'
LT = '<'
GTE = '>='
LTE = '<='

digits = '0123456789'
"""int: Contains the digits that are supported by the lexer"""

types = {
    'int' : 'Integer', #String literal int
    'float' : 'Float', #String literal float
    '+' : 'PLUS',
    '-' : 'MINUS',
    '*' : 'MULTIPLY',
    '/' : 'DIVIDE',
    '%' : 'MODULO',
    '^' : 'RAISED TO',
    '(' : 'LPAREN',
    ')' : 'RPAREN',
}
"""dict: Contains data types, operators and other special characters"""

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
"""str: The alphabet for the programming language"""

reserved_words = {}
"""dict: Contains the reserved words for the programming langauge"""

keywords = ["keyword", "token", "var", "and", "or", "not", "if", "then", "elif", "else"]
"""list: Contains the keywords for the programming language"""
