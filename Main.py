import sys
from antlr4 import *
from gen.GrammarLexer import GrammarLexer
from gen.GrammarParser import GrammarParser
from gen.GrammarVisitor import *
from SimplePrinter import SimplePrinter


def main():
    input_stream = FileStream('Test.txt')
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.file_input()
    visitor = SimplePrinter()
    visitor.visit(tree)


if __name__ == '__main__':
    main()
