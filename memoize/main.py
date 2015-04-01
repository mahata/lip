#!/usr/bin/env python

from backtracklexer import BacktrackLexer
from backtrackparser import BacktrackParser
from sys import argv

if __name__ == "__main__":
    lexer = BacktrackLexer(argv[1] + "\0")
    parser = BacktrackParser(lexer)
    parser.stat()
