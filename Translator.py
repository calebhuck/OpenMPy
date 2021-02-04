from antlr_parser.GrammarVisitor import *
from antlr_parser.GrammarParser import GrammarParser


class Translator(GrammarVisitor):
    def visitSimple_stmt(self, ctx: GrammarParser.Simple_stmtContext):
        #print('simple statement')
        return self.visitChildren(ctx)

    def visitFor_stmt(self, ctx: GrammarParser.For_stmtContext):
        #print('for statement')
        return self.visitChildren(ctx)

    def visitOmp_stmt(self, ctx: GrammarParser.For_stmtContext):
        #print('omp statement')
        thread_num = ctx.getChild(ctx.getChildCount())
        print('threadnum = ', thread_num)
        for x in ctx.getChildren():
            print(x.getText())
        return self.visitChildren(ctx)

    def visitThread_num(self, ctx: GrammarParser.Thread_numContext):

        return ctx.NUMBER()