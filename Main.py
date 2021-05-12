from ompy.antlr_generated.GrammarLexer import GrammarLexer
from ompy.antlr_generated.GrammarVisitor import *
from ompy.antlr_generated.GrammarParser import GrammarParser
from ompy.Translator import Translator
from ompy.source_printer import SourcePrinter

#needed for exec, import stmts don't work from string, will be required in input file later
#from ompy.omp_functions import *
#from ompy.runtime import *

def main():
    input_stream = FileStream('directive_tests/single.py')
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    #print(stream.getText())
    parser = GrammarParser(stream)
    tree = parser.file_input()
    printer = SourcePrinter()
    visitor = Translator(printer)
    visitor.visit(tree)
    print(printer.get_source(), '\n\n\n')
    #exec(printer.get_source())
    with open('output.py', 'w') as f:
        f.write(printer.get_source())

    '''from subprocess import Popen, PIPE

    process = Popen(['jython', './testing_input/output.py'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    #print(stdout, '\n', stderr)'''


if __name__ == '__main__':
    main()
