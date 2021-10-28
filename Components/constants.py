TYPE_EOF = 'End of file'
"""str: The end of file constant"""

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
    '(' : 'LPAREN',
    ')' : 'RPAREN'
}
"""dict: Contains data types, operators and other special characters"""

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
"""str: The alphabet for the programming language"""

reserved_words = {}
"""dict: Contains the reserved words for the programming langauge"""

keywords = ["keyword", "token"]
"""list: Contains the keywords for the programming language"""
