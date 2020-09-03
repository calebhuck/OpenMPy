# Generated from C:/Users/Caleb/PycharmProjects/OpenMPy\Hello.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
        buf.write("\22\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\5\2\13\n\2\3\3\3\3")
        buf.write("\3\3\5\3\20\n\3\3\3\2\2\4\2\4\2\2\2\21\2\n\3\2\2\2\4\17")
        buf.write("\3\2\2\2\6\7\7\3\2\2\7\b\7\5\2\2\b\13\5\4\3\2\t\13\7\2")
        buf.write("\2\3\n\6\3\2\2\2\n\t\3\2\2\2\13\3\3\2\2\2\f\r\7\4\2\2")
        buf.write("\r\20\7\5\2\2\16\20\7\2\2\3\17\f\3\2\2\2\17\16\3\2\2\2")
        buf.write("\20\5\3\2\2\2\4\n\17")
        return buf.getvalue()


class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'hello'", "'bye'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "ID", "WS" ]

    RULE_rule1 = 0
    RULE_rule2 = 1

    ruleNames =  [ "rule1", "rule2" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    ID=3
    WS=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Rule1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HelloParser.ID, 0)

        def rule2(self):
            return self.getTypedRuleContext(HelloParser.Rule2Context,0)


        def EOF(self):
            return self.getToken(HelloParser.EOF, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_rule1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule1" ):
                listener.enterRule1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule1" ):
                listener.exitRule1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule1" ):
                return visitor.visitRule1(self)
            else:
                return visitor.visitChildren(self)




    def rule1(self):

        localctx = HelloParser.Rule1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_rule1)
        try:
            self.state = 8
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HelloParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.match(HelloParser.T__0)
                self.state = 5
                self.match(HelloParser.ID)
                self.state = 6
                self.rule2()
                pass
            elif token in [HelloParser.EOF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 7
                self.match(HelloParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HelloParser.ID, 0)

        def EOF(self):
            return self.getToken(HelloParser.EOF, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_rule2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule2" ):
                listener.enterRule2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule2" ):
                listener.exitRule2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule2" ):
                return visitor.visitRule2(self)
            else:
                return visitor.visitChildren(self)




    def rule2(self):

        localctx = HelloParser.Rule2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_rule2)
        try:
            self.state = 13
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HelloParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.match(HelloParser.T__1)
                self.state = 11
                self.match(HelloParser.ID)
                pass
            elif token in [HelloParser.EOF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 12
                self.match(HelloParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





