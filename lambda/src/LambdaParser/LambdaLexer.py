# Generated from /home/johannes/Workspace/lambda/src/LambdaParser/Lambda.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write(";\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\6\6 \n\6\r\6\16\6!\3\6\3\6\3\7\6\7\'\n\7\r")
        buf.write("\7\16\7(\3\b\6\b,\n\b\r\b\16\b-\3\t\5\t\61\n\t\3\t\3\t")
        buf.write("\3\n\6\n\66\n\n\r\n\16\n\67\3\n\3\n\3!\2\13\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\3\2\5\4\2C\\c|\3\2\62")
        buf.write(";\4\2\13\13\"\"\2?\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\3\25\3\2\2\2\5\27\3\2\2\2\7\31\3")
        buf.write("\2\2\2\t\33\3\2\2\2\13\35\3\2\2\2\r&\3\2\2\2\17+\3\2\2")
        buf.write("\2\21\60\3\2\2\2\23\65\3\2\2\2\25\26\7?\2\2\26\4\3\2\2")
        buf.write("\2\27\30\7*\2\2\30\6\3\2\2\2\31\32\7+\2\2\32\b\3\2\2\2")
        buf.write("\33\34\7.\2\2\34\n\3\2\2\2\35\37\7]\2\2\36 \13\2\2\2\37")
        buf.write("\36\3\2\2\2 !\3\2\2\2!\"\3\2\2\2!\37\3\2\2\2\"#\3\2\2")
        buf.write("\2#$\7_\2\2$\f\3\2\2\2%\'\t\2\2\2&%\3\2\2\2\'(\3\2\2\2")
        buf.write("(&\3\2\2\2()\3\2\2\2)\16\3\2\2\2*,\t\3\2\2+*\3\2\2\2,")
        buf.write("-\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\20\3\2\2\2/\61\7\17\2\2")
        buf.write("\60/\3\2\2\2\60\61\3\2\2\2\61\62\3\2\2\2\62\63\7\f\2\2")
        buf.write("\63\22\3\2\2\2\64\66\t\4\2\2\65\64\3\2\2\2\66\67\3\2\2")
        buf.write("\2\67\65\3\2\2\2\678\3\2\2\289\3\2\2\29:\b\n\2\2:\24\3")
        buf.write("\2\2\2\b\2!(-\60\67\3\b\2\2")
        return buf.getvalue()


class LambdaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    ID = 5
    METHODNAME = 6
    INT = 7
    NEWLINE = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "ID", "METHODNAME", "INT", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "ID", "METHODNAME", "INT", 
                  "NEWLINE", "WS" ]

    grammarFileName = "Lambda.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


