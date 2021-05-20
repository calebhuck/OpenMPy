from ompy.antlr_generated.GrammarLexer import GrammarLexer
from ompy.antlr_generated.GrammarVisitor import *
from ompy.antlr_generated.GrammarParser import GrammarParser
from ompy.Translator import Translator
from ompy.source_printer import SourcePrinter

def main():
    input_stream = FileStream('benchmarks/matrix_multiplication.py')
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.file_input()
    printer = SourcePrinter()
    visitor = Translator(printer)
    visitor.visit(tree)
    print(printer.get_source(), '\n\n\n')
    with open('output.py', 'w') as f:
        f.write(printer.get_source())

if __name__ == '__main__':
    main()
