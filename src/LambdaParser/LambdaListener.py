# Generated from /home/johannes/Workspace/lambda/src/LambdaParser/Lambda.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LambdaParser import LambdaParser
else:
    from LambdaParser import LambdaParser

# This class defines a complete listener for a parse tree produced by LambdaParser.
class LambdaListener(ParseTreeListener):

    # Enter a parse tree produced by LambdaParser#prog.
    def enterProg(self, ctx:LambdaParser.ProgContext):
        pass

    # Exit a parse tree produced by LambdaParser#prog.
    def exitProg(self, ctx:LambdaParser.ProgContext):
        pass


    # Enter a parse tree produced by LambdaParser#printExpr.
    def enterPrintExpr(self, ctx:LambdaParser.PrintExprContext):
        pass

    # Exit a parse tree produced by LambdaParser#printExpr.
    def exitPrintExpr(self, ctx:LambdaParser.PrintExprContext):
        pass


    # Enter a parse tree produced by LambdaParser#assign.
    def enterAssign(self, ctx:LambdaParser.AssignContext):
        pass

    # Exit a parse tree produced by LambdaParser#assign.
    def exitAssign(self, ctx:LambdaParser.AssignContext):
        pass


    # Enter a parse tree produced by LambdaParser#variable.
    def enterVariable(self, ctx:LambdaParser.VariableContext):
        pass

    # Exit a parse tree produced by LambdaParser#variable.
    def exitVariable(self, ctx:LambdaParser.VariableContext):
        pass


    # Enter a parse tree produced by LambdaParser#int.
    def enterInt(self, ctx:LambdaParser.IntContext):
        pass

    # Exit a parse tree produced by LambdaParser#int.
    def exitInt(self, ctx:LambdaParser.IntContext):
        pass


    # Enter a parse tree produced by LambdaParser#parens.
    def enterParens(self, ctx:LambdaParser.ParensContext):
        pass

    # Exit a parse tree produced by LambdaParser#parens.
    def exitParens(self, ctx:LambdaParser.ParensContext):
        pass


    # Enter a parse tree produced by LambdaParser#methodCall.
    def enterMethodCall(self, ctx:LambdaParser.MethodCallContext):
        pass

    # Exit a parse tree produced by LambdaParser#methodCall.
    def exitMethodCall(self, ctx:LambdaParser.MethodCallContext):
        pass


    # Enter a parse tree produced by LambdaParser#exprList.
    def enterExprList(self, ctx:LambdaParser.ExprListContext):
        pass

    # Exit a parse tree produced by LambdaParser#exprList.
    def exitExprList(self, ctx:LambdaParser.ExprListContext):
        pass



del LambdaParser