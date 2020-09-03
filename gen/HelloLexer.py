# Generated from C:/Users/Caleb/PycharmProjects/OpenMPy\Hello.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write("!\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\4\6\4\27\n\4\r\4\16\4\30\3")
        buf.write("\5\6\5\34\n\5\r\5\16\5\35\3\5\3\5\2\2\6\3\3\5\4\7\5\t")
        buf.write("\6\3\2\4\3\2c|\5\2\13\f\17\17\"\"\2\"\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\3\13\3\2\2\2\5\21\3\2")
        buf.write("\2\2\7\26\3\2\2\2\t\33\3\2\2\2\13\f\7j\2\2\f\r\7g\2\2")
        buf.write("\r\16\7n\2\2\16\17\7n\2\2\17\20\7q\2\2\20\4\3\2\2\2\21")
        buf.write("\22\7d\2\2\22\23\7{\2\2\23\24\7g\2\2\24\6\3\2\2\2\25\27")
        buf.write("\t\2\2\2\26\25\3\2\2\2\27\30\3\2\2\2\30\26\3\2\2\2\30")
        buf.write("\31\3\2\2\2\31\b\3\2\2\2\32\34\t\3\2\2\33\32\3\2\2\2\34")
        buf.write("\35\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\37\3\2\2\2")
        buf.write("\37 \b\5\2\2 \n\3\2\2\2\5\2\30\35\3\b\2\2")
        return buf.getvalue()


class HelloLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    ID = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'hello'", "'bye'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "ID", "WS" ]

    grammarFileName = "Hello.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


