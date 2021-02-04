import sys
sys.path.append("./")
from antlr_parser.GrammarLexer import GrammarLexer
from antlr_parser.GrammarParser import GrammarParser
from antlr_parser.GrammarVisitor import *
from Translator import Translator


def main():
    input_stream = FileStream('Test.txt')
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.file_input()
    visitor = Translator()
    visitor.visit(tree)


if __name__ == '__main__':
    main()
