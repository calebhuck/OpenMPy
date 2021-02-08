from antlr_parser.GrammarVisitor import *
from antlr_parser.GrammarParser import GrammarParser


class Translator(GrammarVisitor):
    def visitSimple_stmt(self, ctx:GrammarParser.Simple_stmtContext):
        count = ctx.getChildCount()

        return self.visitChildren(ctx)

    def visitCompound_stmt(self, ctx:GrammarParser.Compound_stmtContext):
        #print(ctx.getText())
        return self.visitChildren(ctx)

    def visitOmp_stmt(self, ctx:GrammarParser.For_stmtContext):
        #print('omp statement')
        for x in ctx.getChildren():
            #print(x.getText())]
            pass
        return self.visitChildren(ctx)

    def visitComp_op(self, ctx:GrammarParser.Comp_opContext):
        print(' ', ctx.getText(), ' ')

    def visitYield_expr(self, ctx:GrammarParser.Yield_exprContext):
        #print(ctx.getChildCount())
        #print(ctx.getChild(0).getText())
        print(ctx.YIELD())
        print(ctx.)