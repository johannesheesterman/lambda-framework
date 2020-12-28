from LambdaInterpeter.ScriptEngines.ScriptEngine import ScriptEngine
import os
from typing import List
from LambdaInterpeter.ScriptEngines.PythonScriptEngine.PythonScriptEngine import PythonScriptEngine
from LambdaParser.LambdaVisitor import LambdaVisitor
from LambdaParser.LambdaParser import LambdaParser

class LambdaInterpeter(LambdaVisitor):

    __script_paths= [ 'scripts' ]
    __script_engines:List[ScriptEngine]  = []

    def __init__(self):
        self.memory = {}
        self.__load_script_engines()

    def visitAssign(self, ctx:LambdaParser.AssignContext):
        id = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[id] = value
        print(self.memory)

    def visitVariable(self, ctx:LambdaParser.VariableContext):
        return self.memory[ctx.ID().getText()]

    def visitInt(self, ctx:LambdaParser.IntContext):
        return int(ctx.INT().getText())

    def visitParens(self, ctx:LambdaParser.ParensContext):
        return self.visit(ctx.expr())
    
    def visitMethodCall(self, ctx:LambdaParser.MethodCallContext):
        methodName = ctx.METHODNAME().getText()
        arguments = self.visit(ctx.exprList())
        for engine in self.__script_engines:
            if engine.isMethodDefined(methodName):
                return engine.executeMethod(methodName, arguments)
        raise Exception(f"Method '{methodName}' not found")

    def visitExprList(self, ctx:LambdaParser.ExprListContext):
        return [ self.visit(expr) for expr in ctx.expr() ]

    def __load_script_engines(self) -> None:
        self.__script_engines.append(PythonScriptEngine(self.__script_paths, "py"))

