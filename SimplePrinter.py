from gen.GrammarVisitor import *
from gen.GrammarParser import GrammarParser


class SimplePrinter(GrammarVisitor):
    def visitSimple_stmt(self, ctx:GrammarParser.Simple_stmtContext):
        print('simple statement')
        return self.visitChildren(ctx)
    def visitFor_stmt(self, ctx:GrammarParser.For_stmtContext):
        print('for statmet')
        return self.visitChildren(ctx)
