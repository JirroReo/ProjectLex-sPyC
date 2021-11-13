TYPE_EOF = 'End of file'
"""str: The end of file constant"""

digits = '0123456789'
"""int: Contains the digits that are supported by the lexer"""

delimiters = {
    ' ' : 'SPACE',
    ';' : 'SEMICOLON',
    ',' : 'COMMA',
    '\n': 'NEWLINE',
    '\t': 'TAB'
}
special_characters = {
    '.' : 'PERIOD',
    '#' : 'COMMENT',
    '(' : 'LPAREN',
    ')' : 'RPAREN',
    '+' : 'PLUS',
    '-' : 'MINUS',
    '*' : 'MULTIPLY',
    '/' : 'DIVIDE',
    '%' : 'MODULO',
    '^' : 'POWER',
    '\\': 'BACKSLASH',
    "'" : 'APOSTROPHE',
    '"' : 'QUOTE',
    '!' : 'EXCLAMATION',
    '[' : 'LBRACKET',
    ']' : 'RBRACKET',
    '{' : 'LBRACE',
    '}' : 'RBRACE',
    '>' : 'GREATER',
    '<' : 'LESS',
    '=' : 'ASSIGN'
}
"""dict: operators and other special characters"""

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
"""str: The alphabet for the programming language"""

types = {
    'int' : 'INTEGER', #String literal int
    'float' : 'FLOAT', #String literal float
    'string': 'STRING'
}
"""dict: Contains data types"""

reserved_words = {}
"""dict: Contains the reserved words for the programming langauge"""

keywords = [
    'as',
    'assert',
    'break',
    'bool',
    'char',
    'class',
    'continue',
    'def',
    'del',
    'otherwise',
    'except',
    'finally',
    'False',
    'for',
    'from',
    'global',
    'whenever',
    'import',
    'in',
    'is',
    'lambda',
    'nonlocal',
    'None',
    'pass',
    'raise',
    'return',
    'True',
    'try',
    'with',
    'while',
    'yield'
]
"""list: Contains keywords"""
