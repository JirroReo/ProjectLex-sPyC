from Lexer.lexer import Lexer
from Parser.parser import Parser

def run(fn, text):
    # Analyze lexigraph
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error: return None, error
    # return tokens, error
    # ^ [Uncomment if gonna use Lexicographical Analyzer]

    # v [Turn block into comment if gonna use Parser]
    # Generate Abstract Syntax Tree 
    parser = Parser(tokens)
    ast = parser.parse()
    return ast.node, ast.error

if __name__ == "__main__":
    while True:
        text = input('lex > ')
        result, error = run('<stdin>', text)

        if error: print(error.__str__())
        else: print(result)
        # else: print(*result, sep="\n")