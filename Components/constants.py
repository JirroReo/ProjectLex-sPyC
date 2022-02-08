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
    '//' : 'FLOORDIVIDE',
    '>' : 'GREATER',
    '<' : 'LESS',
    '=' : 'ASSIGN',
    '>=': 'GREATEROREQUAL',
    '<=': 'LESSOREQUAL',
    '==': 'EQUAL',
    '!=': 'NOTEQUAL',
    '+=': 'PLUSASSIGN',
    '-=': 'MINUSASSIGN',
    '*=': 'MULTIPLYASSIGN',
    '/=': 'DIVIDEASSIGN',
    '%=': 'MODULOASSIGN',
    '^=': 'POWERASSIGN',
    '&&': 'LOGICALAND',
    '||': 'LOGICALOR',
    '&' : 'AND',
    '|' : 'OR',
    '!' : 'NOT',
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

reserved_words = [
]

"""list: Contains the reserved words for the programming langauge"""

keywords = [
    'as',
    'assert',
    'break',
    'bool',
    'boolean', # HAHA Boolboolean
    'char',
    'character',
    'class',
    'continue',
    'def',
    'define',
    'del',
    'delete',
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
    'int',
    'integer',
    'lambda',
    'nonlocal',
    'None',
    'pass',
    'raise',
    'read',
    'return',
    'True',
    'try',
    'with',
    'while',
    'within',
    'write',
    'yield',
    'if',
    'else'
]
"""list: Contains keywords"""
