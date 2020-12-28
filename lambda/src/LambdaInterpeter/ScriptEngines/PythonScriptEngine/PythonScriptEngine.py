
import ast
from typing import List
from LambdaInterpeter.ScriptEngines.ScriptEngine import ScriptEngine


class PythonScriptEngine(ScriptEngine):
    
    def __init__(self, script_paths, fileExtension):
        ScriptEngine.__init__(self, script_paths, fileExtension)
    
    def __list_methods_in_file__(self, filename):
        with open(filename, "r") as source:
            tree = ast.parse(source.read())    
            return [function.name for function in tree.body if isinstance(function, ast.FunctionDef)]

    def __execute_method__(self, filename:str, methodName:str, args: List[any]) -> any:
        with open(filename, "r") as source:
            tree = ast.parse(source.read(), mode='exec')    
            code = compile(tree, filename='_', mode='exec')
            namespace = {}
            exec(code, namespace)
            result = namespace[methodName](*args)
            return result
        