import Lex.lex as lex

while True:
    text = input('lex > ')
    result, error = lex.run(text)

    if error: print(error.as_string())
    else: print(result)
    # else: print(*result, sep="\n")