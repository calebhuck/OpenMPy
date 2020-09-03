from gen.HelloListener import *
from gen.HelloParser import HelloParser


class Rule1Printer(HelloListener):
    def enterRule1(self, ctx: HelloParser.Rule1Context):
        print("enter rule 1")

    def exitRule1(self, ctx:HelloParser.Rule1Context):
        print("exit rule 1")

    def enterRule2(self, ctx: HelloParser.Rule1Context):
        print("enter rule 2")

    def exitRule2(self, ctx:HelloParser.Rule2Context):
        print('exit rule 2')