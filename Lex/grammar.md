### Project Lex

#### Grammar Rules


| Name                   | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| expression             | term ((PLUS|MINUS) term)*                                                   |
| term                   | factor ((MOD|MUL|DIV) factor)*                                                  |
| factor                 | INT|FLOAT                             |


