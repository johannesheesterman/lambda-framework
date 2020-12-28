# Generated from /home/johannes/Workspace/lambda/src/LambdaParser/Lambda.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LambdaParser import LambdaParser
else:
    from LambdaParser import LambdaParser

# This class defines a complete generic visitor for a parse tree produced by LambdaParser.

class LambdaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LambdaParser#prog.
    def visitProg(self, ctx:LambdaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaParser#printExpr.
    def visitPrintExpr(self, ctx:LambdaParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaParser#assign.
    def visitAssign(self, ctx:LambdaParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaParser#variable.
    def visitVariable(self, ctx:LambdaParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaParser#int.
    def visitInt(self, ctx:LambdaParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaParser#parens.
    def visitParens(self, ctx:LambdaParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaParser#methodCall.
    def visitMethodCall(self, ctx:LambdaParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaParser#exprList.
    def visitExprList(self, ctx:LambdaParser.ExprListContext):
        return self.visitChildren(ctx)



del LambdaParser