from ompy.antlr_generated.GrammarLexer import GrammarLexer
from ompy.antlr_generated.GrammarVisitor import *
from ompy.antlr_generated.GrammarParser import GrammarParser
from ompy.Translator import Translator
from ompy.source_printer import SourcePrinter

from contextlib import redirect_stdout
from io import StringIO
import sys
def main():
    err_output = StringIO()
    sys.stderr = err_output
    try:
        input_stream = FileStream('/Users/calebhuck/PycharmProjects/OpenMPy/benchmarks/matrix_multiplication.py')
    except FileNotFoundError:
        print('aha')
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.file_input()
    printer = SourcePrinter()
    visitor = Translator(printer)
    visitor.visit(tree)
    if err_output.getvalue() != '':
        print(err_output.getvalue())
    else:
        print(printer.get_source())
    with open('output.py', 'w') as f:
        f.write(printer.get_source())

if __name__ == '__main__':
    main()
