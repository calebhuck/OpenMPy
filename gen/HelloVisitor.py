# Generated from C:/Users/Caleb/PycharmProjects/OpenMPy\Hello.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser

# This class defines a complete generic visitor for a parse tree produced by HelloParser.

class HelloVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HelloParser#rule1.
    def visitRule1(self, ctx:HelloParser.Rule1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#rule2.
    def visitRule2(self, ctx:HelloParser.Rule2Context):
        return self.visitChildren(ctx)



del HelloParser