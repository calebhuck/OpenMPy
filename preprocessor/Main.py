import os
from ompy.antlr_generated.GrammarLexer import GrammarLexer
from ompy.antlr_generated.GrammarVisitor import *
from ompy.antlr_generated.GrammarParser import GrammarParser
from ompy.Translator import Translator
from ompy.source_printer import SourcePrinter

from contextlib import redirect_stdout
from io import StringIO
import sys


def main():
    if len(sys.argv) != 2:
        raise Exception('Wrong number of command line arguments from jython: this shouln\'t happen')
    #print('file name: ', sys.argv[1])
    filename = sys.argv[1]

    j_home = os.getenv('JYTHON_HOME')
    if j_home[:-1] != '/':
        j_home = j_home + '/'

    err_output = StringIO()
    sys.stderr = err_output
    try:
        input_stream = FileStream(filename)
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
        print('import sys')
        print('sys.path.append(\'' + j_home + 'preprocessor/ompy\')')
        print(printer.get_source())
    #with open('output.py', 'w') as f:
    #    f.write(printer.get_source())

if __name__ == '__main__':
    main()
