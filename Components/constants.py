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

constants = [
    'MathPi',
    'PhysicsSIGravity',
    'ChemRydberg',
    'TimeSinD'
]

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
    '===': 'STRICTEQUAL',
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
    'string': 'STRING',
    'bool' : 'BOOL',
    'boolean' : 'BOOLEAN',
    'char' : 'CHAR',
    'character': 'CHARACTER' 
}

boolean_literal = [
    'True',
    'False'
]


"""dict: Contains data types"""

reserved_words = [
    'goto',
    'quit'
]

"""list: Contains the reserved words for the programming langauge"""

keywords = [
    'const',
    'as',
    'assert',
    'break',
    'class',
    'continue',
    'def',
    'define',
    'del',
    'delete',
    'otherwise',
    'except',
    'finally',
    'for',
    'from',
    'global',
    'whenever',
    'import',
    'int',
    'integer',
    'lambda',
    'nonlocal',
    'None',
    'pass',
    'raise',
    'read',
    'return',
    'try',
    'while',
    'within',
    'write',
    'yield',
    'if',
    'else'
]
"""list: Contains keywords"""
