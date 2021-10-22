## Project Lex
===========

###  Architecture

This project is built using these libraries/softwares:

- [Python](https://www.python.org/)

### Structure

Important folders/file in this project:

- `shell.py` : Main driver file
- `Lex/` : Most of what drives the project lives here
- `Lex/lexer.py` : Main Lexer file
- `Lex/parser.py` : Main Parser file
- `Lex/tokens.py` : Where the Token object can be found
- `Lex/constants.py` : All constants here, such as regexs, objects, tokens, keywords
- `Lex/errors.py` : All types of errors here, such as IllegalCharacterError

### Setting up the project

#### Clone this repo

```
$ git clone <repo-url> ProjectLex
$ cd ProjectLex
```

#### Running the project

On the base project directory:
`python3 shell.py`
