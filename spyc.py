from Lexer.lexer import Lexer
from Parser.parser import Parser
import sys

def analyze_source(fn, text, isParser=False):
    if isParser:
        result, error = run_parser(fn, text)
    else:
        result, error = run_lexer(fn, text)

    if error: print(error.__str__())
    else: print(result)

def run_parser(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error: return None, error
    return tokens, error

def run_lexer(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error: return None, error
    parser = Parser(tokens)
    ast = parser.parse()
    return ast.node, ast.error

if __name__ == "__main__":
    if('-f' in sys.argv or '--file' in sys.argv): # checks if the option f is provided as a command line argument
        fileOptionIdx = sys.argv.index('-f') if ('-f' in sys.argv) else sys.argv.index('--file') #file option index
        fileOptionArgIdx = fileOptionIdx + 1 # file option argument index

        # ensures that an file option argument is given and that it does not start with '-'
        filename = sys.argv[fileOptionArgIdx] if len(sys.argv) > fileOptionArgIdx and sys.argv[fileOptionArgIdx][0] != '-' else False
        print(str(sys.argv))
        if(filename): #if the filename is not false
            print('filename: ', filename) #output the file name
            if(filename.lower().endswith('.spyc')):
                try: # 
                    with open(filename, 'r') as f: #Open the file
                        text = f.read() # get the whole text in the file
                        if('-p' in sys.argv or '--parser' in sys.argv):
                            analyze_source(filename, text, True) # run the parser and syntax analyzer 
                        else:
                            analyze_source(filename, text, False) # run the lexical and syntax analyzer 

                except FileNotFoundError: #catch the error when FileNotFoundError occurs
                    print('File not found!')
            else: print('Please provide a file that ends with .spyc')
        else: # invalid or missing argument for file option
            print("Missing or invalid argument for option -f")

    else: # if no command line argument is provided
        while True:
            text = input('sPyC > ')
            analyze_source('<stdin>', text)
            # else: print(*result, sep="\n")
