from os import name
from typing import List
import js2py
from LambdaInterpeter.ScriptEngines.ScriptEngine import ScriptEngine

class JavaScriptScriptEngine(ScriptEngine):

    def __init__(self, script_paths, fileExtension):
        ScriptEngine.__init__(self, script_paths, fileExtension)
    
    def __list_methods_in_file__(self, filename):
        with open(filename, "r") as source:
            context = js2py.parse_js(source.read())
            return [function['id']['name'] for function in context['body'] if function['type'] == 'FunctionDeclaration']

    def __execute_method__(self, filename:str, methodName:str, args: List[any]) -> any:
       with open(filename, "r") as source:
            namespace = js2py.EvalJs({'python_sum': sum})  
            namespace.execute(source.read())
            return namespace[methodName](*args)