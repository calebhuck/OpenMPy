import sys
sys.path.append("./")
from antlr_parser.GrammarLexer import GrammarLexer
from antlr_parser.GrammarVisitor import *
from antlr_parser.GrammarParser import GrammarParser
from Translator import Translator
from printer.Printer import Printer


def main():
    input_stream = FileStream('Test.py')
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    #print(stream.getText())
    parser = GrammarParser(stream)
    tree = parser.file_input()
    printer = Printer()
    visitor = Translator(printer)
    visitor.visit(tree)
    print(printer.get_source())


if __name__ == '__main__':
    main()
