from Lexer.lexer import Lexer
from Parser.parser import Parser
from Interpreter.interpreter import Interpreter
from Components.context import Context
from Components.symboltable import SymbolTable
from Components.number import Number
import sys

global_symbol_table = SymbolTable()
global_symbol_table.set("NULL", Number(0))
global_symbol_table.set("TRUE", Number(1))
global_symbol_table.set("FALSE", Number(0))

def analyze_source(fn, text):
    result, error = run(fn, text)

    if error: print(error.__str__())
    elif result: print(result)

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
    if ast.error: return None, ast.error

    # Interpreter block, must have Parser enabled
    interpreter = Interpreter()
    context = Context('<program>') #root parent of tracebacks in errors, placeholder <program>
    context.symbol_table = global_symbol_table
    result = interpreter.visit(ast.node, context)

    return result.value, result.error

if __name__ == "__main__":
    if('-f' in sys.argv): # checks if the option f is provided as a command line argument
        fileOptionIdx = sys.argv.index('-f') #file option index
        fileOptionArgIdx = fileOptionIdx + 1 # file option argument index

        # ensures that an file option argument is given and that it does not start with '-'
        filename = sys.argv[fileOptionArgIdx] if len(sys.argv) > fileOptionArgIdx and sys.argv[fileOptionArgIdx][0] != '-' else False

        if(filename): #if the filename is not false
            print('filename: ', filename) #output the file name
            try: # 
                with open(filename, 'r') as f: #Open the file
                    text = f.read() # get the whole text in the file
                    analyze_source(filename, text) # run the lexical and syntax analyzer 

            except FileNotFoundError: #catch the error when FileNotFoundError occurs
                print('File not found!')
        else: # invalid or missing argument for file option
            print("Missing or invalid argument for option -f")

    else: # if no command line argument is provided
        while True:
            text = input('sPyC >>> ')
            if text == "\q": break
            analyze_source('<stdin>', text)
            # else: print(*result, sep="\n")
