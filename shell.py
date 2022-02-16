from Lexer.lexer import Lexer
from Components.tokens import print_tokens, to_symbol_table
from Parser.parser import Parser
from Interpreter.interpreter import Interpreter
from Components.errors import Context
import sys
import os


def analyze_source(fn, text):
    result, error = run(fn, text)
    if error: print(error.__str__())
    # else: print_tokens(result)
    else: return result

def run(fn, text):
    # Analyze lexigraph
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error: return None, error

    # return tokens, error
    # ^ [Lexer] Uncomment line 23 for Lexer

    # v [Parser]
    # Generate Abstract Syntax Tree 
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error: return None, ast.error

    # Interpreter block, must have Parser enabled
    interpreter = Interpreter()
    context = Context('<program>') #root parent of tracebacks in errors, placeholder <program>
    result = interpreter.visit(ast.node, context)

    return result.value, result.error
    # parser = Parser(tokens)
    # ast = parser.parse()
    # return ast.node, ast.error

def write_to_file(tokens):
    fileOptionIdx = sys.argv.index('-o') #file option index
    fileOptionArgIdx = fileOptionIdx + 1 # file option argument index

    # ensures that an file option argument is given and that it does not start with '-'
    filename = sys.argv[fileOptionArgIdx] if len(sys.argv) > fileOptionArgIdx and sys.argv[fileOptionArgIdx][0] != '-' else False

    if(not(filename)): #if the filename is not false
        filename = 'symbolTable'

    if(not(filename.endswith('.txt'))):
        filename += '.txt'
    
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write(format('TOKENS', '>15') + '       ' + 'LEXEMES' + '\n')
        f.write('------------------------------------------\n')
        f.write(to_symbol_table(tokens))

if __name__ == "__main__":
    tokens = [] #variable for the token arrays

    if('-f' in sys.argv or '--filename' in sys.argv): # checks if the option f is provided as a command line argument
        fileOptionIdx = sys.argv.index('-f') if ('-f' in sys.argv) else sys.argv.index('--filename') #file option index
        fileOptionArgIdx = fileOptionIdx + 1 # file option argument index

        # ensures that an file option argument is given and that it does not start with '-'
        filepath = sys.argv[fileOptionArgIdx] if len(sys.argv) > fileOptionArgIdx and sys.argv[fileOptionArgIdx][0] != '-' else False
        head, filename = os.path.split(filepath)

        if(filepath): #if the filename is not false
            if(filename.lower().endswith('.spyc')):
                print('filename: ', filename) #output the file name
                print('\n')
                print(format('TOKENS', '>15'), '    ', 'LEXEMES')
                print('------------------------------------------')


                try: # 
                    with open(filepath, 'r') as f: #Open the file
                        text = f.read() # get the whole text in the file
                        tokens = analyze_source(filepath, text) # run the lexical and syntax analyzer 

                except FileNotFoundError: #catch the error when FileNotFoundError occurs
                    print('File not found!')
            else: print('Invalid file format, please use a .spyc file.')
        else: # invalid or missing argument for file option
            print("Missing or invalid argument for option -f")

    else: # if no command line argument is provided
        while True:
            text = input('sPyC >>> ')
            if text == "quit()": break
            tokens = analyze_source('<stdin>', text)
            if tokens:
                print(tokens)
                if('-o' in sys.argv):
                    write_to_file(tokens)

    if('-o' in sys.argv):
        write_to_file(tokens)
