from antlr_parser.GrammarVisitor import *
from antlr_parser.GrammarParser import GrammarParser


class Translator(GrammarVisitor):
    def visitSimple_stmt(self, ctx:GrammarParser.Simple_stmtContext):
        #print('simple statement')
        return self.visitChildren(ctx)

    def visitFor_stmt(self, ctx:GrammarParser.For_stmtContext):
        #print('for statement')
        return self.visitChildren(ctx)

    def visitOmp_stmt(self, ctx:GrammarParser.For_stmtContext):
        #print('omp statement')
        for x in ctx.getChildren():
            print(x.getText())
        return self.visitChildren(ctx)
