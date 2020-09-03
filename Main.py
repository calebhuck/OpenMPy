import sys
from antlr4 import *
from gen.HelloLexer import HelloLexer
from gen.HelloParser import HelloParser
from gen.HelloListener import *
from Rule1Printer import Rule1Printer


def main():
    input_stream = FileStream('Test.txt')
    lexer = HelloLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)
    tree = parser.rule1()
    printer = Rule1Printer()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main()