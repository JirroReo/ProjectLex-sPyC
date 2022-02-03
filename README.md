## sPyC
===========

###  Architecture

The language is designed with the idea of low-level like C but user-friendly like Python, the goal is for it to be attractive to non-programmers but also be very powerful to experienced programmers.

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

On the base project directory run any:
```
python3 spyc.py
```

```
python spyc.py
```
```
python spyc.py -f <file.spyc> -o <outputfilename>
```
```
./spyc
```

### Assignments

| Role                   | Names                                                                       |
|------------------------|-----------------------------------------------------------------------------|
| Coding                 | Crisostomo, Joseph Karl                                                     |
|                        | Reoloso, Jirro Dave                                                         |
|                        | Villanueva, Ian Kirk                                                        |
| Documentation          | Concepcion, Freanne Lei                                                     |
|                        | Delos Santos, Rons Marie                                                    |
|                        | Fernandez, Mikaela                                                          |
|                        | Martinez, John Lloyd                                                        |
