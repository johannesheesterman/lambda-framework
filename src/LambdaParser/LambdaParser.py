# Generated from /home/johannes/Workspace/lambda/src/LambdaParser/Lambda.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("\62\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2")
        buf.write("\16\2\r\3\3\3\3\5\3\22\n\3\3\3\3\3\3\3\3\3\5\3\30\n\3")
        buf.write("\5\3\32\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4%\n")
        buf.write("\4\3\4\5\4(\n\4\3\5\3\5\3\5\7\5-\n\5\f\5\16\5\60\13\5")
        buf.write("\3\5\2\2\6\2\4\6\b\2\2\2\66\2\13\3\2\2\2\4\31\3\2\2\2")
        buf.write("\6\'\3\2\2\2\b)\3\2\2\2\n\f\5\4\3\2\13\n\3\2\2\2\f\r\3")
        buf.write("\2\2\2\r\13\3\2\2\2\r\16\3\2\2\2\16\3\3\2\2\2\17\21\5")
        buf.write("\6\4\2\20\22\7\n\2\2\21\20\3\2\2\2\21\22\3\2\2\2\22\32")
        buf.write("\3\2\2\2\23\24\7\7\2\2\24\25\7\3\2\2\25\27\5\6\4\2\26")
        buf.write("\30\7\n\2\2\27\26\3\2\2\2\27\30\3\2\2\2\30\32\3\2\2\2")
        buf.write("\31\17\3\2\2\2\31\23\3\2\2\2\32\5\3\2\2\2\33(\7\7\2\2")
        buf.write("\34(\7\t\2\2\35\36\7\4\2\2\36\37\5\6\4\2\37 \7\5\2\2 ")
        buf.write("(\3\2\2\2!\"\7\b\2\2\"$\7\4\2\2#%\5\b\5\2$#\3\2\2\2$%")
        buf.write("\3\2\2\2%&\3\2\2\2&(\7\5\2\2\'\33\3\2\2\2\'\34\3\2\2\2")
        buf.write("\'\35\3\2\2\2\'!\3\2\2\2(\7\3\2\2\2).\5\6\4\2*+\7\6\2")
        buf.write("\2+-\5\6\4\2,*\3\2\2\2-\60\3\2\2\2.,\3\2\2\2./\3\2\2\2")
        buf.write("/\t\3\2\2\2\60.\3\2\2\2\t\r\21\27\31$\'.")
        return buf.getvalue()


class LambdaParser ( Parser ):

    grammarFileName = "Lambda.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "METHODNAME", "INT", "NEWLINE", 
                      "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_exprList = 3

    ruleNames =  [ "prog", "stat", "expr", "exprList" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    ID=5
    METHODNAME=6
    INT=7
    NEWLINE=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LambdaParser.StatContext)
            else:
                return self.getTypedRuleContext(LambdaParser.StatContext,i)


        def getRuleIndex(self):
            return LambdaParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = LambdaParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.stat()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LambdaParser.T__1) | (1 << LambdaParser.ID) | (1 << LambdaParser.METHODNAME) | (1 << LambdaParser.INT))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LambdaParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LambdaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LambdaParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(LambdaParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LambdaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LambdaParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(LambdaParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(LambdaParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = LambdaParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = LambdaParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.expr()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LambdaParser.NEWLINE:
                    self.state = 14
                    self.match(LambdaParser.NEWLINE)


                pass

            elif la_ == 2:
                localctx = LambdaParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.match(LambdaParser.ID)
                self.state = 18
                self.match(LambdaParser.T__0)
                self.state = 19
                self.expr()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LambdaParser.NEWLINE:
                    self.state = 20
                    self.match(LambdaParser.NEWLINE)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LambdaParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LambdaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LambdaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LambdaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LambdaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LambdaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(LambdaParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class MethodCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LambdaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def METHODNAME(self):
            return self.getToken(LambdaParser.METHODNAME, 0)
        def exprList(self):
            return self.getTypedRuleContext(LambdaParser.ExprListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodCall" ):
                listener.enterMethodCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodCall" ):
                listener.exitMethodCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = LambdaParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LambdaParser.ID]:
                localctx = LambdaParser.VariableContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(LambdaParser.ID)
                pass
            elif token in [LambdaParser.INT]:
                localctx = LambdaParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(LambdaParser.INT)
                pass
            elif token in [LambdaParser.T__1]:
                localctx = LambdaParser.ParensContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.match(LambdaParser.T__1)
                self.state = 28
                self.expr()
                self.state = 29
                self.match(LambdaParser.T__2)
                pass
            elif token in [LambdaParser.METHODNAME]:
                localctx = LambdaParser.MethodCallContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.match(LambdaParser.METHODNAME)
                self.state = 32
                self.match(LambdaParser.T__1)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LambdaParser.T__1) | (1 << LambdaParser.ID) | (1 << LambdaParser.METHODNAME) | (1 << LambdaParser.INT))) != 0):
                    self.state = 33
                    self.exprList()


                self.state = 36
                self.match(LambdaParser.T__2)
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


    class ExprListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LambdaParser.ExprContext)
            else:
                return self.getTypedRuleContext(LambdaParser.ExprContext,i)


        def getRuleIndex(self):
            return LambdaParser.RULE_exprList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprList" ):
                listener.enterExprList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprList" ):
                listener.exitExprList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = LambdaParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.expr()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LambdaParser.T__3:
                self.state = 40
                self.match(LambdaParser.T__3)
                self.state = 41
                self.expr()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





