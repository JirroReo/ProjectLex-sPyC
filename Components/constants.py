TYPE_EOF = 'End of file'
"""str: The end of file constant"""

digits = '0123456789'
"""int: Contains the digits that are supported by the lexer"""

spaces = {
    ' ' : 'SPACE',
    '\n': 'NEWLINE',
    '\t': 'TAB'
}
"""dict: spaces"""

delimiters = {
    ';' : 'SEMICOLON',
    ',' : 'COMMA',
}
"""dict: delimiters """

operators = {
    '+' : 'PLUS',
    '-' : 'MINUS',
    '*' : 'MULTIPLY',
    '/' : 'DIVIDE',
    '%' : 'MODULO',
    '^' : 'POWER',
    '>' : 'GREATER',
    '<' : 'LESS',
    '=' : 'ASSIGN',
    '>=': 'GREATEROREQUAL',
    '<=': 'LESSOREQUAL',
    '==': 'EQUAL',
    '+=': 'PLUSASSIGN',
    '-=': 'MINUSASSIGN',
    '*=': 'MULTIPLYASSIGN',
    '/=': 'DIVIDEASSIGN',
    '%=': 'MODULOASSIGN',
    '^=': 'POWERASSIGN',
    '&&': 'LOGICALAND',
    '||': 'LOGICALOR',
    '&' : 'AND',
    '|' : 'OR'
}
"""dict: special characters"""

special_characters = {
    '.' : 'PERIOD',
    '#' : 'COMMENT',
    '(' : 'LPAREN',
    ')' : 'RPAREN',
    '\\': 'BACKSLASH',
    "'" : 'APOSTROPHE',
    '"' : 'QUOTE',
    '!' : 'EXCLAMATION',
    '[' : 'LBRACKET',
    ']' : 'RBRACKET',
    '{' : 'LBRACE',
    '}' : 'RBRACE',
}
"""dict: special characters"""

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
    'yield',
    'if',
    'else'
]
"""list: Contains keywords"""
