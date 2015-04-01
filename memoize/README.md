## What's this?

It's based on "Backtracking Parser" described in [Language Implementation Patterns](https://pragprog.com/book/tpdsl/language-implementation-patterns).

## Grammar

```
stat     : list EOF | assign EOF ;
assign   : list '=' list ;
list     : '[' elements ']' ;
elements : element (',' element)* ;
element  : NAME '=' NAME | NAME | list ;
// END: parser

NAME     : LETTER+ ;
LETTER   : 'a'..'z'|'A'..'Z' ;
WS       : (' '|'\t'|'\n'|'\r')+ {skip();} ;
```

## Example

```
python3 main.py "[a, b]"
python3 main.py "[a, b] = [c, d]"
python3 main.py "[a, b"  # Error
```
